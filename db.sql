SQLite format 3   @    4                                                            4 .WJ   � ������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         �<//�qtablesqlb_temp_table_1sqlb_temp_table_1CREATE TABLE "sqlb_temp_table_1" (
	"id"	INTEGER,
	"category"	STRING,
	"name"	STRING,
	"img"	STRING,
	"cost"	FLOAT,
	"cost_med"	FLOAT,
	"cost_sml"	FLOAT,
	"outage"	BOOL,
	"sizable"	BOOL,
	"milk"	BOOL,
	"condiment"	BOOL,
	"purchased"	INTEGER
)�//�Ytablesqlb_temp� �YtableitemsitemsCREATE TABLE "items" (
	"id"	INTEGER,
	"category"	STRING,
	"name"	STRING,
	"img"	STRING,
	"cost"	FLOAT,
	"cost_med"	FLOAT,
	"cost_sml"	FLOAT,
	"outage"	BOOL,
	"sizable"	BOOL,
	"milk"	BOOL,
	"condiment"	BOOL,
	"purchased"	INTEGER
)  s�tableusersusersCREATE TABLE users (

    name STRING, 
    username STRING,
    password STRING,
    role STRING,
    logged INTEGER

    )  ��'tableshiftsshiftsCREATE TABLE shifts (

    date STRING, 
    open BOOL,
    cash FLOAT

    )  u�]tableusersusersCREATE TABLE users (

    n^	�tableentriesentriesCREATE TABLE entries (

    date STRING, 
    metric INTEGER

    )n�7tableordersordersCREATE TABLE orders (

    timestamp STRING, 
    amount FLOAT,
    cash FLOAT

    )  q!!�?tableattributesattributesCREATE TABLE attributes (

    category STRING, 
    name STRING, 
    outage BOOL

    )   ��CtableitemsitemsCREATE TABLE items (
    
    category STRING, 
    name STRING, 
    img STRING, 
    cost FLOAT,
    cost_med FLOAT,
    ^�tableentriesentriesCREATE TABLE entries (

    date STRING, 
    metric INTEGER

    )� � ������scSC3#������                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        20-05-2024!2024-05-26!2024-06-13!2024-06-12!2024-05-26!2024-06-10!2024-06-09!2024-06-08!2024-06-07!2024-06-06
!2024-06-05	!2024-06-04!2024-06-03!2024-06-02!2024-06-01!2024-05-24!2024-05-23!2024-05-21   20-05-202!2024-05-26      �~����J<&��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               !'CONDIMENTSVanilla Syrup!'CONDIMENTSCaramel SyrupMILKNo Milk	MILKAlmondMILKSoy
MILKOat	%MILKLactose FreeMILKSkim!MILKFull-Cream � %CONDIMENTNo Condiment � !CONDIMENTSRaw Sugar!)CONDIMENTSHazelnut Syrup    'CONDIMENTVanilla Sy!%CONDIMENTSNo Condiment!CONDIMENTSSugar      ���tQ.���\9�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             !505/11/2024, 09:30:16@������!504/20/2024, 07:52:34@������!504/20/2024, 07:52:19@������!504/13/2024, 08:46:35@������!504/13/2024, 08:17:41@Q�fffffP!
504/13/2024, 08:17:26@������!	504/13/2024, 08:15:53@������!504/13/2024, 08:15:33@������!504/13/2024, 08:14:50@������!504/13/2024, 08:13:24@������!504/13/2024, 08:11:37@������!504/13/2024, 08:11:18@������!504/13/2024, 08:10:37@������A!504/13/2024, 08:10:15@������!504/13/2024, 08:09:14@������      ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  !John Smithjohn09USER   !Joey Smithjoey �]MNGR      ����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  !	04/13/2024@YVfffff!04/04/2024@�Y����!04/04/2024@!������04/04/24@l�\(�                         ��uQ��
[d@����h
�
�r?	s
'
	�	�	�	O	+����c��LsG#���jF���r6
���Z6���j&���N*���vQ
                                         � 404/04/2024, 12:58:41@333334
�������� 0"W504/04/2024, 12:58:30@ �fffff
� 04/04/2024, 12:57#V504/04/2024, 12:57:40@b�fffff �"U504/04/2024, 12:57:07@+L�����"T504/04/2024, 12:56:12@=�fffff� 0"S504/04/2024, 12:53:21@"�fffff 0"R504/04/2024, 12:53:18@ �fffff2� 04/04/2024, 1"Q504/04/2024, 12:53:13@������4"P504/04/2024, 12:53:01@ �fffff2"504/04/2024, 11:08:09@"������2"O504/04/2024, 12:52:57@0�fffff2"N504/04/2024, 12:52:53@������"M504/04/2024, 12:52:50@������"L504/04/2024, 12:52:47@������"K504/04/2024, 12:52:44@�������1504/04/2024, 12:24:04$ �"J504/04/2024, 12:48:14@������
"I504/04/2024, 12:48:08@������
"H504/04/2024, 12:48:05@������
"G504/04/2024, 12:48:02@������
~ 04/04/2024, 12:47"F504/04/2024, 12:47:59@������Z"E504/04/2024, 12:47:55@������U"D504/04/2024, 12:47:42@������
.  04/04/2024, 12:47:39@���"C504/04/2024, 12:47:39@������2"B504/04/2024, 12:47:35@������
"A504/04/2024, 12:47:32@������
"@504/04/2024, 12:47:29@������Z 0"?504/04/2024, 12:47:23@������� 04/04/2024, 12:38">504/04/2024, 12:38:43@������
"=504/04/2024, 12:38:35@!������
"<504/04/2024, 12:38:30@!������

 0";504/04/2024, 12:37:19@"3333346 0":504/04/2024, 12:37:14@!������� 04/04/202"9504/04/2024, 12:36:52@������<"8504/04/2024, 12:36:46@;Y������ 04/04/202"7504/04/2024, 12:36:35@������
"6504/04/2024, 12:36:19@������k 04/04/2024, 12:33#5504/04/2024, 12:33:26@@�fffff �"4504/04/2024, 12:33:18@!������
"3504/04/2024, 12:30:35@������� 0"2504/04/2024, 12:24:09@6s333332 004/04/2024, 12:24:04$ ��\ 04/04/202"0504/04/2024, 12:23:56@M      d"/504/04/2024, 12:23:27@������	 04/04".504/04/2024, 11:28:25@F�333342" 504/04/2024, 11:09:12@!������
"-504/04/2024, 11:28:06@������",504/04/2024, 11:23:29@������"+504/04/2024, 11:23:01@������"*504/04/2024, 11:22:52@������")504/04/2024, 11:20:59@������
K 04/04/2024, 1"(504/04/2024, 11:15:55@@�fffff)"'504/04/2024, 11:15:47@*�33334"!504/04/2024, 11:09:52@!������
"&504/04/2024, 11:15:34@������"%504/04/2024, 11:13:54@������"$504/04/2024, 11:11:56@������"#504/04/2024, 11:10:51@������""504/04/2024, 11:10:17@������
� 04/04/202"504/04/2024, 10:54:04@������
"X504/04/2024, 12:58:41@333334

� 04/04/20#504/04/2024, 11:03:52@c�33332 �"504/04/2024, 11:05:52@������� m04/04/2024, 11:03:52@c�33332 ��E�33338� @04/04/2024, 11:03:35@�������ᙙ����� 804/04/2024, 1"504/04/2024, 11:03:35@������"504/04/2024, 11:02:07@������"504/04/2024, 11:01:30@������"504/04/2024, 11:00:18@������"504/04/2024, 10:59:28@������"504/04/2024, 10:57:23@������"504/04/2024, 10:56:39@������"504/04/2024, 10:54:53@������ <04/04/2024, 10:54:04@������
�333333 04/04/202"504/04/2024, 10:15:28@A������P#504/04/2024, 09:23:03@6@      �9 0"504/04/2024, 09:21:00@!������� 04/04/2024, 09:11"504/04/2024, 09:11:11@������"504/04/2024, 09:10:50@6@     "504/04/2024, 08:56:50@*�33334A 04/04/2024, 08:56"504/04/2024, 08:56:04@������"504/04/2024, 08:55:57@!������
"504/04/2024, 08:50:02@*�33334xm 0"
504/04/2024, 08:49:56@*�33334� 04/04/202"	504/04/2024, 08:47:22@!������
"504/04/2024, 08:46:42@!������
� #504/04/2024, 08:42:44@c������ �#504/04/2024, 08:43:30@c33333 �#504/04/2024, 08:43:29@c33333 �#504/04/2024, 08:43:28@c33333 �#504/04/2024, 08:43:27@c33333 �#504/04/2024, 08:43:18@c33333 �   504/04/2024, 08:42:44@c������ �@E������   0#504/03/2024, 16:59:35@c33333 �      ����?|��U�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                M!!1			HOT_DRINKSFlat Whiteitems/no-image.png@������@      @������E1		DESSERTSCakeitems/no-image.png@ �fffff@������@������H!1			HOT_DRINKSLatteitems/no-image.png@������@      @������0#1			COLD_DRINKSWateritems/no-image.pngQ#)1			COLD_DRINKSIced Chocolateitems/no-image.png@������@      @������B
#+1			
COLD_DRINKSIced Long Blackitems/no-image.png@������M	#!1				COLD_DRINKSIced Mochaitems/no-image.png@������@      @������M#!1			COLD_DRINKSIced Latteitems/no-image.png@������@      @������e E!1		DESSERTSFruit Cakeitems/no-image.png@"�fffff@������@K!1		DESSERTSFruit Cakeitems/no-image.png@"�fffff@������@������L%1			DESSERTSBanana Breaditems/no-image.png@ �fffff@������@������L!!1				HOT_DRINKSLong Blackitems/no-image.png@������@      @������   N!!1				HOT_DRINKSFlat Whiteitems/no-image.png@������@      @������K	!!1				HOT_DRINKSCappuccinoitems/no-image.png@������@      @������