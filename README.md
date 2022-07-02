# vae-22-project

Headphone Equalization Filter
Compensation filters are linear-pahase FIR filters of length 2048 samples at a sampling rate 44.1 kHz calculated with high-shelf regularisation in the frequency domain.

### TODOs

- [x] Visualize headphone recordings (as facet)
- [x] Visualize impulse responses
- [x] Read code for compensation filters
- [] Implement filter
- [] Apply filter for each heaphone
- [] Visualize filtered recordings
- [] Do hearing test
- [] Compare results
- [] Outcomes
- [] Start with report
- [] Prepare slides

### Steps (for each Headphone and L|R Channels)

- [x] Transfer IRs to freq domain
- [x] Take the complex mean of each (L|R)
- [x] Design bandpass filter (D)
- [x] Design the regularisation filter (B)
- [x] Calculate Inverse Filter (with the formula) for each headphone (L|R)
- [x] Transform back to time domain
- [] Try out with DAW | convolve directly in Jupyter notebook

### MatLab Filter Pseduo code

- Define global parameters
  - clen -> length of compensation filter
  - wlen -> length of window for raw IR measurements
  - fc -> upper corner frequency
  - beta -> regularization effort
  - one_filter -> (boolean) L|R ear averaged OR different filters for L|R
- Choose headphones:
  - create a variable (boolean) for each headphone to select one
- Load headphone measurements for each headphone
  - Collected indices (L|R recordings) for each headphone
- Window and select IRs
  - normalize all IRs (separate for each headphone)
  - window IRs and truncate to target length
  - Plot all unprocessed HpIRs and window
  - Plot all unprocessed and windowed HpTFs
  - Pick selected windowed IRs
- Calculate Complex Mean of Selected HpTFs
  - one_filter == 1
  - one_filter == 0
  - normalize IRs
  - fft of IRs
  - complex mean
  - Plot processed and mean transfer function
- Design target bandpass
  - fl -> lower corner freq
  - fh -> upper corner freq
  - stopatt -> stopband attenuation
  - Find beta for kaiser window to satisfy desired stopband attenuation
  - Plot target bandpass IR and frequency response
- Design regularisation filter (high-shelf
  - Plot regularisation filter
- Calculate inverse filter in the freq. domain
  - Plot inverse filter
- Calculate compensation results
  - Plot results for one_filter == 1
  - Plot results for one_filter == 0
- Save compensation filters
