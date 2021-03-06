# HpTF compensation filters
This repository holds HpTF (headphone transfer function) compensation filters for use in binaural synthesis for several headphone types that have been created by the Matlab script [Calc_HpTF_compensation_filter.m](http://github.com/spatialaudio/hptf-compensation-filters/blob/master/Calc_HpTF_compensation_filter.m) out of the measurement data in folder [measurements](http://github.com/spatialaudio/hptf-compensation-filters/tree/master/compensation_filters).

## Method for calculation of compensation filters
Compensation filters are linear-phase FIR filters of length 2048 samples at a sampling rate of 44.1 kHz calculated with high-shelf regularisation in the frequency domain. Confer the following papers for details on this method:
* Schärer, Z. and Lindau, A. (2009): Evaluation of Equalization Methods for Binaural Synthesis. Proc. of the 126th AES Convention
* Norcross, S. G, Soulodre, G. A. and Lavoie, M. C. (2004): Distortion Audibility in Inverse Filtering. Proc. of the 117th AES Convention
* Kirkeby, O., Nelson, P. A., Hamada, H. and Orduna-Bustamante, F. (1998): Fast Deconvolution of Multichannel Systems using Regularization. IEEE Trans. on Speech and Audio Proc. 6(2), pp. 189-195

## HpTF Measurements
The HpTF measurements have been performed on a KEMAR 45BA dummy head with large ears with a sweep of order 2^19 with bass emphasis at a sampling rate of 44.1 kHz. HpTFs are available for the following headphone types:
* Sennheiser HD 600
* Thomson HED415N
* AKG K271 MKII
* AKG K601
* AKG K612 PRO

## Choice of compensation filters
As you most likely are not in possession of a headphone with a specific serial number, it is recommended to use the filters containing the term "1Filter" in the file name. These filters are averaged out of measurements of the left and right channel for one or more headphones of the same type, that is the filters for left and right channel are the same. This bears the additional advantage that the slight (approx. 0.5 dB) level difference between left and right HpTFs due to different installation depths of the KEMAR microphones is not falsely compensated for. The different installation depths lead only to a level difference due to the inverse square law which is here only of importance for very close sources which is the case when measuring HpTFs.

The term "LRFilter" in the file name denotes compensation filters that are made for a headphone with a specific serial number with different filters for the left and right channel.

## Licenses
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />The data by Matthias Geier and Vera Erbes in this repository is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

The Matlab code by Vera Erbes is licensed under the MIT license. Confer header of [Calc_HpTF_compensation_filter.m](http://github.com/spatialaudio/hptf-compensation-filters/blob/master/Calc_HpTF_compensation_filter.m) for more information on this license.
