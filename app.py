from config import Config
from rtlsdr import RtlSdr
import signal, sys
from models import Sample
from database import session
import logging
import matplotlib.pyplot as plt
from matplotlib.mlab import psd


config = Config()

def signal_handler(signal, frame):
    logging.info('Exiting on SIGINT...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def plot_samples(samples):
    # Plot
    plt.figure()
    # Compute the power spectral density
    power, psd_freqs = plt.psd(samples, NFFT=1024, Fs=config.sample_rate/1e6)
    
    # Adjust x-axis to be centered around the center frequency
    psd_freqs = psd_freqs + config.center_freq/1e6
    
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Relative power (dB)')
    plt.savefig('output.png')

def main():


    sdr = RtlSdr()
    sdr.sample_rate = config.sample_rate
    sdr.center_freq = config.center_freq
    sdr.freq_correction = config.freq_correction
    sdr.gain = config.gain
    batch_size = config.batch_size

    try:
        while True:
            samples = sdr.read_samples(256*1024)
            plot_samples(samples)
            
            for i, sample in enumerate(samples):
                new_sample = Sample(real_part=sample.real, imag_part=sample.imag)
                session.add(new_sample)
                
                if (i+1) % batch_size == 0:
                    session.commit()
                    logging.info("Committed to db a batch of {batch_size} samples")

    except KeyboardInterrupt:
        logging.info("Interrupted by User")

    finally:
        # Ensure resources are cleaned up whether or not an exception occurred
        session.close()
        sdr.close()

if __name__ == "__main__":
    main()

