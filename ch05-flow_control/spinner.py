import asyncio
import itertools
import sys

async def spin(msg):  
    write, flush = sys.stdout.write, sys.stdout.flush # <1>
    for char in itertools.cycle('|/-\\'): # <2>
        status = char + ' ' + msg
        write(status)     
        flush()
        write('\x08' * len(status))   # <3>
        try:
            await asyncio.sleep(.1)  # <4>
        except asyncio.CancelledError:  # <5>
            break
    write(' ' * len(status) + '\x08' * len(status)) #<6>

async def slow_function():  # <7>
    # pretend waiting a long time for I/O
    await asyncio.sleep(3) 
    return 42

async def supervisor():  # <8>
    # before python 3.7
    #spinner = asyncio.ensure_future(spin('thinking!'))    
    spinner = asyncio.create_task(spin('thinking!'))  # <9>
    #spinner = await spin('thinking!')
    print('spinner object:', spinner)  # <10>
    result = await slow_function()  # <11>
    spinner.cancel()  # <12>
    return result

def main():
    # before python 3.7
    #loop = asyncio.get_event_loop() 
    #result = loop.run_until_complete(supervisor()) 
    #loop.close()
    result = asyncio.run(supervisor())  # <13>    
    print('Answer:', result)

if __name__ == '__main__':
    main()