**SINR-Prediction-Calculator**

A tool for predicting the SINR (Signal-to-Interference-plus-Noise Ratio) in wireless communication systems, based on received signal power, interference power, and bandwidth.

**Overview**
The SINR-Prediction-Calculator allows users to compute SINR, which is crucial for evaluating the performance of wireless networks. SINR is a key metric that helps in assessing the quality of a communication link by accounting for both interference and noise in the system.

**Features**
**Calculate SINR:** Predict SINR based on the received signal power, interference power, and noise.
**Multiple Interference Sources:** Supports calculation when multiple interference sources are present.
**Flexible Inputs:** Allows users to adjust parameters for system analysis and optimization.
**Performance Evaluation:** Helps evaluate network reliability and efficiency.

**Formula**
The SINR is calculated using the following formula:
![image](https://github.com/user-attachments/assets/f55b3020-c22c-40d5-a385-4a25b10cfca6)

**Usage**
**Inputs**
**Reciever Signal Power (dBm):** The power of the desired signal received by the system.
**Interference Power (dBm):** The power of interfering signals in the environment.
**Bandwidth (MHz):** The system's bandwidth, used to calculate noise power.

**Output**
**SINR (dB):** The computed SINR value, which indicates the quality of the communication link.

**Example**

**Installation**
Clone this repository and install any necessary dependencies.
git clone https://github.com/AmruthGudigar111/SINR-Prediction-Calculator.git
cd SINR-Prediction-Calculator
pip install -r requirements.txt


