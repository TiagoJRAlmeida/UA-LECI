-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE UpdateEmpresa
    @NIF CHAR(9),
    @Nome NVARCHAR(100),
    @Endereco NVARCHAR(200),
    @Telefone NVARCHAR(20),
    @Email NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @RowCount INT = 0;

    BEGIN TRY
        BEGIN TRANSACTION
            UPDATE GP_Empresa
            SET Nome = @Nome,
                Endereco = @Endereco,
                Telefone = @Telefone,
                Email = @Email
            WHERE NIF = @NIF;

            SET @RowCount = @@ROWCOUNT;
        COMMIT TRANSACTION;
        
        RETURN @RowCount;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION;

        THROW;
    END CATCH
END
GO
