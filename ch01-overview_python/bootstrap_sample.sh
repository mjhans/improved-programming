#!/bin/zsh

printmsg() {
  echo -e "\033[1;34m$1\033[0m"
}

SPARK_VERSION="2.3.4"
PYTHON_VERSION="3.6.10"
SCALA_VERSION="2.11"
ZSHRC_PATH="$HOME/.zshrc"

update_homebrew() {
  which -s brew
  if [[ $? != 0 ]]; then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  fi
  brew update
}

install_basic_env() {
  update_homebrew
  brew install cask
  echo 'export PATH="/usr/local/opt/gettext/bin:$PATH"' >> $ZSHRC_PATH
  echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> $ZSHRC_PATH
  source $ZSHRC_PATH

  brew install cask docker

  brew tap AdoptOpenJDK/openjdk
  brew install cask adoptopenjdk8
  echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)' >> $ZSHRC_PATH
  echo 'export PATH="$JAVA_HOME:$PATH"' >> $ZSHRC_PATH
  source $ZSHRC_PATH

  brew install cask jetbrains-toolbox
  brew install scala@$1
  echo 'export SCALA_HOME="/usr/local/opt/scala@'$1'/libexec"' >> $ZSHRC_PATH
  echo 'export PATH="$SCALA_HOME/bin:$PATH"' >> $ZSHRC_PATH
  source $ZSHRC_PATH

  brew install maven
}

uninstall_basic_env() {
  update_homebrew
  brew uninstall scala@$1
  brew uninstall maven
  brew uninstall cask jetbrains-toolbox
  brew uninstall cask adoptopenjdk8
  brew untap AdoptOpenJDK/openjdk
  brew uninstall cask docker
  brew uninstall cask

  sed -i '' '/export PATH=\"\/usr\/local\/opt\/gettext\/bin:\$PATH\"/d' $ZSHRC_PATH
  sed -i '' '/export PATH=\"\/usr\/local\/opt\/openssl@1.1\/bin:\$PATH\"/d' $ZSHRC_PATH

  sed -i '' '/export SCALA_HOME=\"\/usr\/local\/opt\/scala\@'$1'\/libexec"/d' $ZSHRC_PATH
  sed -i '' '/export PATH=\"\$SCALA_HOME\/bin:\$PATH\"/d' $ZSHRC_PATH

  sed -i '' '/export JAVA_HOME=\$(\/usr\/libexec\/java_home -v 1.8)/d' $ZSHRC_PATH
  sed -i '' '/export PATH=\"\$JAVA_HOME:\$PATH\"/d' $ZSHRC_PATH
  source $ZSHRC_PATH
}


install_pyenv() {
  update_homebrew
  brew install pyenv

  echo '#pyenv' >> $ZSHRC_PATH
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $ZSHRC_PATH
  echo 'eval "$(pyenv init -)"' >> $ZSHRC_PATH
  source $ZSHRC_PATH

  pyenv install $1
  pyenv global $1

  brew install pyenv-virtualenv
  echo 'eval "$(pyenv virtualenv-init -)"' >> $ZSHRC_PATH
  source $ZSHRC_PATH

  pip install -U pip
}

uninstall_pyenv() {
  update_homebrew
  pyenv uninstall -f $1

  sed -i '' '/#pyenv/d' $ZSHRC_PATH
  sed -i '' '/export PYENV_ROOT=/d' $ZSHRC_PATH
  sed -i '' '/eval \"$(pyenv init -)\"/d' $ZSHRC_PATH
  sed -i '' '/eval \"$(pyenv virtualenv-init -)\"/d' $ZSHRC_PATH

  brew uninstall -f pyenv-virtualenv
  brew uninstall -f pyenv
  source $ZSHRC_PATH
}

install_spark() {
  update_homebrew

  brew tap eddies/spark-tap
  brew install apache-spark@$1
  echo 'export SPARK_HOME=$(brew --prefix apache-spark@'$1')/libexec' >> $ZSHRC_PATH
  echo 'export SPARK_MASTER_IP=127.0.0.1' >> $ZSHRC_PATH
  echo 'export SPARK_LOCAL_IP=127.0.0.1' >> $ZSHRC_PATH
  echo 'export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH' >> $ZSHRC_PATH
  echo 'export PYTHONPATH="${SPARK_HOME}/python/:${SPARK_HOME}/python/lib/py4j-*-src.zip:${PYTHONPATH}"' >> $ZSHRC_PATH

  source $ZSHRC_PATH
}

uninstall_spark() {
  update_homebrew

  brew uninstall -f apache-spark@$1
  brew untap eddies/spark-tap
  sed -i '' '/export SPARK_HOME=\$(brew --prefix apache-spark@'$1')\/libexec/d' $ZSHRC_PATH
  sed -i '' '/export SPARK_MASTER_IP=127.0.0.1/d' $ZSHRC_PATH
  sed -i '' '/export SPARK_LOCAL_IP=127.0.0.1/d' $ZSHRC_PATH
  sed -i '' '/export PYTHONPATH=\$SPARK_HOME\/python:\$PYTHONPATH/d' $ZSHRC_PATH
  sed -i '' '/export PYTHONPATH=\"\${SPARK_HOME}\/python\/:\${SPARK_HOME}\/python\/lib\/py4j-\*-src.zip:\${PYTHONPATH}"/d' $ZSHRC_PATH

  source $ZSHRC_PATH
}

install_jupyter() {
  pip install jupyter
  echo 'export PYSPARK_DRIVER_PYTHON=$(which jupyter)' >> $ZSHRC_PATH
  echo 'export PYSPARK_DRIVER_PYTHON_OPTS="notebook"' >> $ZSHRC_PATH

  source $ZSHRC_PATH
}

uninstall_jupyter() {
  pip uninstall -y jupyter
  sed -i '' '/export PYSPARK_DRIVER_PYTHON=/d' $ZSHRC_PATH
  sed -i '' '/export PYSPARK_DRIVER_PYTHON_OPTS=/d' $ZSHRC_PATH

  source $ZSHRC_PATH
}


if [ "$1" = "--uninstall" ]; then
  uninstall_jupyter
  uninstall_spark $SPARK_VERSION
  uninstall_pyenv $PYTHON_VERSION
  uninstall_basic_env $SCALA_VERSION
else
  printmsg "backup zshrc"
  if [ -f $ZSHRC_PATH ]; then
    BACKUP_PATH=$ZSHRC_PATH"_backup_$(date +%Y%m%d_%H%M%S)"
    cp $ZSHRC_PATH $BACKUP_PATH
  fi
  printmsg "** install homebrew ..."
  update_homebrew
  
  printmsg "** Install Java8, Scala(2.11), Maven(Java package manager) and IntelliJ..."
  install_basic_env $SCALA_VERSION

  printmsg "** python with pyenv..."
  install_pyenv $PYTHON_VERSION

  printmsg "** Install spark and pyspark..."
  install_spark $SPARK_VERSION
  install_jupyter
fi
