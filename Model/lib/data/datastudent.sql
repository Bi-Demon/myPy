USE master
	go

if EXISTS (select* from sys.databases where name= 'infstudent')
	drop database infstudent
	go

create database infstudent
go

use infstudent
go

--- Tạo table quản lý thông tin sinh viên
create table sinhvien(
	masv		CHAR(10) PRIMARY KEY,
	HO			NVARCHAR(15),
	Ten			NVARCHAR(7),
	ngaysinh	date,

--- 0: Nữ, Nam: 1
	GTINH		bit,
	DIACHI		NTEXT,
	SDT			CHAR(10)
)
go

--- Tạo table quản lý mail đăng nhập sinh viên
create table mailsv(
	masv	CHAR(10) PRIMARY KEY,
	Email	varchar(75),
	PASS	varchar(75)
)
go

ALTER TABLE dbo.mailsv 
	ADD CONSTRAINT FK_mailsv FOREIGN KEY(masv) REFERENCES dbo.sinhvien(masv)