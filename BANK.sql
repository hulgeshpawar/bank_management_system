
create database BMS_DB1;

USE BMS_DB1;

-- CUSTOMER_PERSONAL_INFORMATION
create table CUSTOMER_PERSONAL_INFO
(
  CUSTOMER_ID varchar(5),
  CUSTOMER_NAME varchar(30),
  DATE_OF_BIRTH date,
  GUARDIAN_NAME varchar(30),
  ADDRESS varchar(50),
  CONTACT_NO bigint(10),
  MAIL_ID varchar(20),
  GENDER char(1),
  MARITAL_STATUS varchar(10),
  IDENTIFICATION_DOC_TYPE varchar(20),
  ID_DOC_NO varchar(10),
  CITIZENSHIP varchar(15),
  constraint CUST_PERS_INFO_PK primary key (CUSTOMER_ID)
  );
  
--  show tables;
-- CUSTOMER_REFERNCE-INFORMATION
create table CUSTOMER_REFERENCE_INFO
(
CUSTOMER_ID varchar(5),
REFERENCE_ACC_NAME varchar(30),
REFERENCE_ACC_NO bigint(16),
REFERENCE_ACC_ADDRESS varchar(50),
RELATION varchar(10),
constraint CUST_REF_INFO_PK primary key (CUSTOMER_ID),
constraint CUST_REF_INFO_FK foreign key(CUSTOMER_ID) references CUSTOMER_PERSONAL_INFO(CUSTOMER_ID)
);

create 


