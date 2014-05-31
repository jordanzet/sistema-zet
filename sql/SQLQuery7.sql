USE [SISTEMA-ZET]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Cajero](
	[Id_cajero] [int] NOT NULL,
	[Clave_cajero] [varchar](15) NOT NULL,
	[Cod_tienda] [int] NOT NULL,
	[Nombre_cajero] [varchar](30) NOT NULL,
	[Apellidos_cajero] [varchar](30) NOT NULL,
	[Dni_cajero] [varchar](8) NOT NULL,
 CONSTRAINT [PK_Cajero] PRIMARY KEY CLUSTERED 
(
	[Id_cajero] ASC,
	[Clave_cajero] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


