import asyncio
import time


async def testa(x):
    print("in test a")
    await asyncio.sleep(3)
    print("resuming a")
    return x


async def testb(x):
    print("in test b")
    await asyncio.sleep(1)
    print("resuming b")
    return x


async def main():
    start = time.time()
    resulta = await testa(1)
    resultb = await testb(2)
    print("test a result is %d" % resulta)
    print("test b result is %d" % resultb)
    print("use %s time" % (time.time()-start))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
