USE [SISTEMA-ZET]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Factura_compra](
	[Factura_compra] [int] NOT NULL,
	[Nombre_proveedor] [varchar](30) NOT NULL,
	[Id_jefe_inventario] [int] NOT NULL,
	[Cod_tienda] [int] NOT NULL,
	[Cod_producto] [int] NOT NULL,
	[Fecha_compra] [date] NOT NULL,
	[Detalle] [text] NOT NULL,
	[Importe_neto] [real] NOT NULL,
	[Importe_total] [real] NOT NULL,
 CONSTRAINT [PK_Factura_compra] PRIMARY KEY CLUSTERED 
(
	[Factura_compra] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


