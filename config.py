class Config:
    sample_rate = 2e6  # Hz
    center_freq = 145e6  # Hz
    freq_correction = 60  # PPM
    gain = 'auto'
    db_uri = 'postgresql://postgres:astelit1@89.47.162.7:5432/rtl-sdr'
    batch_size = 262144
