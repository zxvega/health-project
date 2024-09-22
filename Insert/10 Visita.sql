INSERT INTO test.dbo.Visita (fecha,hora,idHospital,idServicio,idMedico,codHist,diagnostico,tratamiento,esIngreso,idCama,fechaAlta) VALUES
	 ('2024-09-01','14:00:00.0000000',1,5,6,100002,N'Bronquitis',N'Antibioticos',0,NULL,'2024-09-01'),
	 ('2024-09-01','15:30:00.0000000',1,5,6,100012,N'Rinitis Alérgica',N'Antihistamínicos',0,NULL,'2024-09-01'),
	 ('2024-09-01','16:09:00.0000000',1,5,6,100004,N'Asma',N'Albuterol y Corticoides',0,NULL,'2024-09-01'),
	 ('2024-09-02','09:15:00.0000000',1,5,8,100009,N'Intolerancia a la Lactosa',N'Dieta: Evitar productos lácteos o optar por alternativas sin lactosa',0,NULL,'2024-09-02'),
	 ('2024-09-02','11:40:00.0000000',1,5,8,100012,N'Gastroenteritis',N'Sueros de Rehidratacion y Ciprofloxacino',0,NULL,'2024-09-02'),
	 ('2024-09-02','07:00:00.0000000',1,1,7,100014,N'Ecografía abdominal : Todo Normal',N'No Aplica',0,NULL,'2024-09-02'),
	 ('2024-09-02','08:30:00.0000000',1,1,7,100016,N'Ecografía de mamas: Todo Normal',N'No Aplica',0,NULL,'2024-09-02'),
	 ('2024-09-02','10:30:00.0000000',1,1,7,100017,N'Ecografía de vesícula biliar: Barro Biliares',N'Recomendacion Consulta con Especialista',0,NULL,'2024-09-02'),
	 ('2024-09-02','14:30:00.0000000',1,1,7,100047,N'Ecografía Abdominal: Hallazgo en el Higado',N'Recomendacion Consulta con Especialista',0,NULL,'2024-09-02'),
	 ('2024-09-02','15:30:00.0000000',1,1,7,100034,N'Ecocardriografia: Todo Normal',N'No Aplica',0,NULL,'2024-09-02');
INSERT INTO test.dbo.Visita (fecha,hora,idHospital,idServicio,idMedico,codHist,diagnostico,tratamiento,esIngreso,idCama,fechaAlta) VALUES
	 ('2024-09-01','14:00:00.0000000',1,6,3,100041,N'Fractura de Tibia y Perone',N'Cirugia con Traumatologo e Internacion',0,NULL,'2024-09-01'),
	 ('2024-09-01','14:30:00.0000000',1,3,4,100041,N'Fractura de Tibia y Perone',N'Cirugia con Traumatologo e Internacion',1,1,'2024-09-03'),
	 ('2024-09-01','09:15:00.0000000',1,6,3,100035,N'Neumonía',N'Internacion con Antibioticos',0,NULL,'2024-09-01'),
	 ('2024-09-01','09:45:00.0000000',1,3,4,100035,N'Neumonía',N'Internacion con Antibioticos',1,2,'2024-09-05'),
	 ('2024-09-01','11:00:00.0000000',1,6,3,100008,N'Apendicitis',N'Cirugia e Internacion',0,NULL,'2024-09-01'),
	 ('2024-09-01','11:30:00.0000000',1,3,4,100008,N'Apendicitis',N'Cirugia e Internacion',1,3,'2024-09-04'),
	 ('2024-09-02','09:00:00.0000000',1,6,3,100046,N'Cálculos renales',N'Cirugia e Internacion',0,NULL,'2024-09-02'),
	 ('2024-09-02','09:30:00.0000000',1,3,4,100046,N'Cálculos renales',N'Cirugia e Internacion',1,4,'2024-09-04'),
	 ('2024-09-02','20:00:00.0000000',1,6,3,100029,N'Infecciones por COVID-19',N'Internacion',0,NULL,'2024-09-02'),
	 ('2024-09-02','20:30:00.0000000',1,3,4,100029,N'Infecciones por COVID-19',N'Internacion',1,5,'2024-09-04');
INSERT INTO test.dbo.Visita (fecha,hora,idHospital,idServicio,idMedico,codHist,diagnostico,tratamiento,esIngreso,idCama,fechaAlta) VALUES
	 ('2024-09-02','13:00:00.0000000',1,6,3,100031,N'Dengue',N'Internacion',0,NULL,'2024-09-02'),
	 ('2024-09-02','13:30:00.0000000',1,3,4,100031,N'Dengue',N'Hidratacion y Control de Fiebre',1,6,'2024-09-04');
