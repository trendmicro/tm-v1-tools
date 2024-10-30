# Overview
This tool was designed to assist SOC managers and IT administrators in analyzing observed attack techniques within their network environment. It automates collecting, processing, and presenting data related to the MITRE ATT&CK tactics and techniques.

# Key Features:
	
## Automated Data Retrieval:
	
The tool automatically fetches data related to observed attack techniques from the Trend Micro XDR API.
		
Users can specify the date range for the data they wish to retrieve, providing flexibility in generating reports for different periods.
	
## Data Processing & Analysis:
			
It processes the retrieved data to count and sort the occurrences of each MITRE technique observed.
		
The tool identifies the top 10 techniques for each MITRE tactic, providing a focused view of the prevalent attack patterns.
	
## Reporting:
	
Generates a comprehensive report in Excel format, including details like technique ID, name, description, and count of occurrences.
		
The report also includes links to the MITRE ATT&CK framework for each technique, facilitating further research and analysis. 

## Benefits:
	
Efficiency: Automates the tedious data collection and analysis process, saving valuable time for cybersecurity professionals.
	
Accuracy: Provides precise and reliable data on observed attack techniques, enhancing the accuracy of security assessments.
	
Insightful: Offers valuable insights into the security landscape, helping organizations effectively understand and mitigate potential threats.


# How to Use:
1. Run the executable file of the OAT Report Generator.
2. Input the API token when prompted (with an option to save it for future use).
3. Specify the number of days of data to retrieve.
4. The tool will fetch, process, and analyze the data, displaying progress bars for each step.
5. Once the process is complete, the tool will save a detailed report in Excel format in the specified location.

# Security Note:
Users are advised to handle API tokens securely and know the security implications of storing tokens locally. Always follow the principle of least privilege and ensure that tokens are accessible only to authorized individuals.

Created by Alejandro Ortiz (Sales Enginneer)