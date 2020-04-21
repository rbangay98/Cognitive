# Cognitive
# ADC Sample #
## Sample rate ##
The sample rate of the ADS1675REF is from 125KSPS to 4MSPS.
The maximum packet size the the ADC software will sample is 1,048,576 samples, however, when sampling at 4MSPS, 
the software will not correctly write 1,048,576 samples. This is most liekely due to the slow hardware that the 
software runs on, and the slow write speeds. A possible solution to this problem is to upgrade the hardware using an SSD.

When sampling at 4MSPS, an appropriate packet size is 160,000. This size gives two full periods of the largest wave (50Hz)
and when sampling at 125KSPS, the maximum 1,048,576 samples will work. using a packet size of approximately 1,000,000 samples
will give 40 periods of the 50Hz wave, approximately 8 seconds per packet.

## tradeoffs ##
Sampling at a higher frequency such as 4MSPS will allow the user to detect much higher frequency signals, up to 2MHz. Sampling at 
125KSPS will limit detection to 62.5KHz. Performing a spectral analysis on the high frequency sampleing rate shows that after 20KHz, 
there is little information. there is however, a spike at 165KHz, of which the cause is currently unknown.

Due to the lack of information past 20KHz, the increased packet size of the 125KSPS samplnig rate appears to be worthwile trade. 
In future, all sampling will be done at 125KSPS, with packet size of 1,000,000 samples.

