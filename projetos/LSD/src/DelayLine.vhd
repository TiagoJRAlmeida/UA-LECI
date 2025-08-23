library IEEE;
use IEEE.std_logic_1164.all;

entity DelayLine is
	port(clk         : in std_logic;	
		  WrData      : in std_logic_vector(7 downto 0);
		  WE          : in std_logic;
		  RST         : in std_logic;
		  DataOut1    : out std_logic_vector(7 downto 0);
		  DataOut2    : out std_logic_vector(7 downto 0);
		  DataOut3    : out std_logic_vector(7 downto 0));
end DelayLine;

architecture behavioral of DelayLine is
	
	--Sinal que vai servir para guardar o valor das nossas 3 saidas.
	--Tem 24 bits porque guarda 3 inputs de 8 bits cada, ou seja, 3*8 = 24.
	signal s_shift : std_logic_vector(23 downto 0) := (others => '0');

begin 
	process(clk)
	begin
		if rising_edge(clk) then
			--Se o reset global for ativado, limpa todos os inputs anteriores, substituindo por 0.
			if (RST = '1') then 
				s_shift <= (others => '0');
			--Caso o enable esteja ativado, que neste caso é o pulso gerado pelo pulse generator,
			--os bits de 0 a 7 são substituidos pelo input vindo da rom, ou seja, é um Shift register á direita.
			elsif (WE = '1') then 
				s_shift <= WrData & s_shift(23 downto 8);
			end if;
		end if;
	end process;
	--Atribuição dos respetivos valores do sinal aos outputs.
	DataOut1 <= s_shift(7 downto 0);
	DataOut2 <= s_shift(15 downto 8);
	DataOut3 <= s_shift(23 downto 16);
end behavioral;