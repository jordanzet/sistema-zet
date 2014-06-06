USE [SISTEMA-ZET]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Factura_venta](
	[Factura_venta] [int] NOT NULL,
	[Nombre_tienda] [varchar](30) NOT NULL,
	[Nombre_cajero] [varchar](30) NOT NULL,
	[Nombre_cliente] [varchar](30) NOT NULL,
	[Fecha_venta] [date] NOT NULL,
	[Detalle] [text] NOT NULL,
	[Importe_total] [real] NOT NULL,
 CONSTRAINT [PK_Factura_venta] PRIMARY KEY CLUSTERED 
(
	[Factura_venta] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


