# Azure-Ecommerce-Big-Data-Engineering-Project
Data Pipeline Using Azure **(Medallion Architecture)** for AI and Data Visualization Processes


![image](https://github.com/user-attachments/assets/c3c2c655-b26b-4802-8b3b-487a6e73accb)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Medallion Architecture**

![image](https://github.com/user-attachments/assets/df7a698c-13a5-46e8-bfe3-9a01b093d344)


![image](https://github.com/user-attachments/assets/ca1efbf0-b93c-4a66-8d99-9ff174eb2c41)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**About the E-commerce Data we are going to use**

 
Kaggle -> https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

![image](https://github.com/user-attachments/assets/76749e29-b1fc-47f7-9a05-18c409b5577e)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Creating the Resource Groups in Azure**

![image](https://github.com/user-attachments/assets/afdb7962-3d3a-4bea-b76b-bfd3fdd8c75a)


![image](https://github.com/user-attachments/assets/b4ca162d-2cac-4034-9f7c-02a4909f77f1)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Storing Data before reading it into Azure Data Factory**

![image](https://github.com/user-attachments/assets/d514a36a-e5f4-44d1-ba33-0094ca8849e7)

![image](https://github.com/user-attachments/assets/1446f2f8-e294-4386-8bc2-02294ac25f2a)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Azure Data Factory (Source)**

![image](https://github.com/user-attachments/assets/abb67c06-a44e-4b35-8b3b-d7f659d84f40)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Azure Data Lake Storage (Sink)**

![image](https://github.com/user-attachments/assets/67e3b1bb-8b69-4ff5-b72f-182ee6fd92f6)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Linking HTTP Data to Azure Data Factory**

![image](https://github.com/user-attachments/assets/de2c3d72-876e-491f-aeb5-0d7dd60573ee)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Linked HTTP Data (From GitHub) and SQL Data (From Filess.io)**

![image](https://github.com/user-attachments/assets/98a9cf69-636a-455b-a54a-1956127e0451)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Bronze Level Reached. Data Pipeline Prepared From Data Sources To Data Factory**

![image](https://github.com/user-attachments/assets/a9c4a0ad-2799-4359-baad-831b90686cbf)




**-----------------------------------------------------------------BRONZE LEVEL ACHIEVED----------------------------------------------------------**





**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Databricks Deployment Done**

![image](https://github.com/user-attachments/assets/b7934745-37fa-4acf-97e3-65d5649d1881)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**App Registration Done to get necessary permissions for Databricks-ADLS connection**

![image](https://github.com/user-attachments/assets/5e456f2a-db18-4342-9e06-f427bf27e27b)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Optional Method to Databricks and ADLS**

![image](https://github.com/user-attachments/assets/cf61ae94-abb5-4c6a-ab81-0afb28aaa8f8)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Access to ADLS Data given to Databricks via App Registration**

![image](https://github.com/user-attachments/assets/800d3f31-8b65-48f3-9c3d-7f4e980cd0fc)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Setting Up Connection with ADLS in Spark Notebook**

![image](https://github.com/user-attachments/assets/12d7ccab-9938-4262-8232-272b8fdd581a)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Installing pymongo library in the Databricks cluster to connect with MongoDB in my Spark Notebook**

![image](https://github.com/user-attachments/assets/ef8ae7f5-64e3-4dc6-8deb-4df2edc5ace7)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Creating Visualizations in Databricks**

![image](https://github.com/user-attachments/assets/a69be52a-4919-4072-aefe-a77859f8ee84)


**---------------------------------------------------------------------------------------------------------------------------------------------------------**



**Data Exported to Silver Layer from Databricks after Data Transformation and Data Enrichment using Spark and MongoDB**

![image](https://github.com/user-attachments/assets/3a339866-b31b-4931-8738-0f05947a9517)



**-----------------------------------------------------------------SILVER LEVEL ACHIEVED----------------------------------------------------------**


**Azure Synapse Setup Issues**

![image](https://github.com/user-attachments/assets/a41f80fb-2ce9-4e06-b26d-0729f57cf0f3)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Azure Synapse Setup Successful**

![image](https://github.com/user-attachments/assets/832b8248-dfc3-4731-891a-f24999f97627)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Access Permission To Synapse to access SILVER data from Azure Data Lake Storage**

![image](https://github.com/user-attachments/assets/ded4724c-4913-4694-a90f-5dc9c4a15f85)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Creating Serverless SQL Pool (Pay-As-You-Go) for reading/querying the data in Azure Synapse**

![image](https://github.com/user-attachments/assets/bbaaa90f-c106-436e-b6d0-96e242dd7c5d)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**Creating a View using SQL in Azure Synapse**

![image](https://github.com/user-attachments/assets/4d111848-51c6-45d9-9501-c87c8a4ce205)

**---------------------------------------------------------------------------------------------------------------------------------------------------------**


**CETAS (Create External Table As Select) to migrate data from Synapse to Gold Layer**

![image](https://github.com/user-attachments/assets/8f1be7cf-29d8-49e7-aedc-915f26ecc866)


**Populated Final Serving Data for AI and Analytics Operations**

![image](https://github.com/user-attachments/assets/a307b48a-38de-4ff3-8f7f-fb190833a424)



**-----------------------------------------------------------------GOLD LEVEL ACHIEVED----------------------------------------------------------**

**-----------------------------------------------------------------Deleting Resource Groups And Final Cleanup----------------------------------------------------------**

![image](https://github.com/user-attachments/assets/9dc1858c-a210-47eb-9272-a5c600595761)







