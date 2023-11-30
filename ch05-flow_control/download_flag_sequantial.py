################################################################################
# python std library                                                           #
################################################################################
import os
import time
import sys

################################################################################
# pip library                                                                  #
################################################################################
import requests

# 인구가 많은 순서의 ISO 3166 국가 코드
# https://en.wikipedia.org/wiki/ISO_3166
# https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
# 
POP20_CC =  ('CN IN US ID BR PK NG BD RU JP '
                'MX PH VN ET EG DE IR TR CD FR').split() 

BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads'

def save_flag(img, filename): 
    # DEST_DIR + "/" + filename으로 이미지 파일 저장
    pass


def get_flag(cc): 
    # requests 모듈의 get 함수를 이용해서 content를 return
    url = f'{BASE_URL}/{cc.lower()}/{cc.lower()}.gif'
    pass

def show(text): 
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list): 
    for cc in sorted(cc_list): 
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = f'\n{count} flags downloaded in {elapsed:.2f}s'
    print(msg)


if __name__ == '__main__':
    main(download_many)

