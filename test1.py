import asyncio
import logging
from rtlsdr import RtlSdr

class SDRContext:
    def __init__(self):
        self.sdr = RtlSdr()

    async def __aenter__(self):
        try:
            await self.sdr.open()
            return self.sdr
        except Exception as e:
            logging.error("Failed to open SDR: %s", str(e))
            raise

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        try:
            await self.sdr.stop()
            self.sdr.close()
        except Exception as e:
            logging.error("Failed to stop SDR: %s", str(e))
            raise

async def streaming():
    async with SDRContext() as sdr:
        try:
            async for samples in sdr.stream():
                # do something with samples
                # ...
                print(samples)
        except KeyboardInterrupt:
            logging.info("Streaming stopped by user")
        except Exception as e:
            logging.error("Streaming error: %s", str(e))

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Run the streaming loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(streaming())
    finally:
        loop.close()

if __name__ == "__main__":
    main()
