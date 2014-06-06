USE [SISTEMA-ZET]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Producto](
	[Cod_producto] [int] NOT NULL,
	[Cod_proveedor] [int] NOT NULL,
	[Cod_tipo_producto] [int] NOT NULL,
	[Cod_area_producto] [int] NOT NULL,
	[Descripción_producto] [varchar](50) NOT NULL,
	[Costo_producto] [real] NOT NULL,
	[Venta_producto] [real] NOT NULL,
	[Stock_producto] [int] NOT NULL,
	[Fecha_ingreso] [date] NOT NULL,
 CONSTRAINT [PK_Productol] PRIMARY KEY CLUSTERED 
(
	[Cod_producto] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


