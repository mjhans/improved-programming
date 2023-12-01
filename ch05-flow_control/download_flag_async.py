################################################################################
# python std library                                                           #
################################################################################
import os
import time
import sys
import asyncio

################################################################################
# pip library                                                                  #
################################################################################
import requests
import aiohttp

################################################################################
# user define library                                                          #
################################################################################
from download_flag_sequantial import BASE_URL, show, POP20_CC, DEST_DIR

CONCUR_REQ = 10

ALL_CC = ('AD AE AF AG AL AM AO AR AT AU AZ BA BB BD BE BF BG BH BI BJ BN BO BR BS BT'
'BW BY BZ CA CD CF CG CH CI CL CM CN CO CR CU CV CY CZ DE DJ DK DM DZ EC EE'
'EG ER ES ET FI FJ FM FR GA GB GD GE GH GM GN GQ GR GT GW GY HN HR HT HU ID'
'IE IL IN IQ IR IS IT JM JO JP KE KG KH KI KM KN KP KR KW KZ LA LB LC LI LK'
'LR LS LT LU LV LY MA MC MD ME MG MH MK ML MM MN MR MT MU MV MW MX MY MZ NA'
'NE NG NI NL NO NP NR NZ OM PA PE PG PH PK PL PT PW PY QA RO RS RU RW SA SB'
'SC SD SE SG SI SK SL SM SN SO SR SS ST SV SY SZ TD TG TH TJ TL TM TN TO TR'
'TT TV TW TZ UA UG US UY UZ VA VC VE VN VU WS YE ZA ZM ZW').split()

async def get_flag(cc):
    url = f'{BASE_URL}/{cc.lower()}/{cc.lower()}.gif'
    async with aiohttp.request('GET', url) as resp:
        return await resp.read()

def save_flag(img, filename): 
    if not os.path.exists(DEST_DIR) :
        os.makedirs(DEST_DIR)
    # DEST_DIR + "/" + filename으로 이미지 파일 저장
    full_path = os.path.join(DEST_DIR,filename)
    with open(full_path, 'wb') as f:
        f.write(img)


async def download_one(cc):
    semphore = asyncio.Semaphore(CONCUR_REQ)
    async with semphore:
        image = await get_flag(cc)
    show(cc)
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, save_flag, image, cc.lower() + '.gif')

    # save_flag(image, cc.lower() + '.gif')
    return cc


async def download_coro(cc_list):
    tasks = (asyncio.create_task(download_one(cc)) for cc in cc_list)
    result = await asyncio.gather(*tasks)
    return result

def download_many(cc_list):
    return len(asyncio.run(download_coro(cc_list)))

def main(download_many):
    t0 = time.time()
    count = download_many(ALL_CC)
    elapsed = time.time() - t0
    msg = f'\n{count} flags downloaded in {elapsed:.2f}s'
    print(msg)

main(download_many)





