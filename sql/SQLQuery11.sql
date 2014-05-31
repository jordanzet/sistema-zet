USE [SISTEMA-ZET]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Jefe_inventario](
	[Id_jefe_inventario] [int] NOT NULL,
	[Clave_jefe_inventario] [varchar](15) NOT NULL,
	[Cod_tienda] [int] NOT NULL,
	[Nombre_jefe_inventario] [varchar](30) NOT NULL,
	[Apellidos_jefe_inventario] [varchar](30) NOT NULL,
	[Dni_jefe_inventario] [varchar](8) NOT NULL,
 CONSTRAINT [PK_Jefe_de_inventario] PRIMARY KEY CLUSTERED 
(
	[Id_jefe_inventario] ASC,
	[Clave_jefe_inventario] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


