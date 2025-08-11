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
-- Author:		Name
-- Create date: 
-- Description:	
-- =============================================
CREATE PROCEDURE AddEmpresa
	-- Add the parameters for the stored procedure here
    @Nome varchar(100),
    @NIF char(9),
    @Endereco varchar(200),
    @Telefone varchar(20),
    @Email varchar(100)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	BEGIN TRY
		BEGIN TRANSACTION
			-- Insert statements for procedure here
			    INSERT INTO GP_Empresa (NIF, Nome, Endereco, Telefone, Email)
				VALUES (@NIF, @Nome, @Endereco, @Telefone, @Email);

				RETURN @@ROWCOUNT;
			COMMIT TRANSACTION
	END TRY
	BEGIN CATCH
		ROLLBACK TRANSACTION
	END CATCH
END
GO
