USE [SISTEMA-ZET]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Administrador](
	[Id_administrador] [int] NOT NULL,
	[Clave_administrador] [varchar](15) NOT NULL,
	[Nombre_administrador] [varchar](30) NOT NULL,
	[Apellidos_administrador] [varchar](30) NOT NULL,
	[Dni_administrador] [varchar](8) NOT NULL,
 CONSTRAINT [PK_Administradoe] PRIMARY KEY CLUSTERED 
(
	[Id_administrador] ASC,
	[Clave_administrador] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


