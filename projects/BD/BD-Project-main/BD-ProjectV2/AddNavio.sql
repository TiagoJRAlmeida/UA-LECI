CREATE PROCEDURE AddNavio
    @Nome varchar(100),
    @Capacidade_Toneladas float,
    @NIF_Empresa char(9)
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        BEGIN TRANSACTION
            INSERT INTO GP_Navio (Nome, Capacidade_Toneladas, NIF_Empresa)
            VALUES (@Nome, @Capacidade_Toneladas, @NIF_Empresa);

   
            SELECT SCOPE_IDENTITY() AS NewID;
			RETURN @@ROWCOUNT;
        COMMIT TRANSACTION
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION
        THROW;
    END CATCH
END
GO