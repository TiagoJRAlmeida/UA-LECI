library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.NUMERIC_STD.all;

entity RamAddr is
	port(clk      	 : in std_logic;	
		  RESET_RAM  : in std_logic;
		  en         : in std_logic;
		  AddressOut : out std_logic_vector(7 downto 0));
end RamAddr;

architecture behavioral of RamAddr is

	signal s_count : natural := 0;

begin 
	process(clk)
	begin
	if rising_edge(clk) then
		--Se o reset da ram for ativado ou o reset global, uma vez que este tambem 
		--ativa o reset da ram, a criação de endereços recomeça do 0.
		if (RESET_RAM = '1') then
			s_count <= 0;
		--Apenas cria os endereços caso o enable esteja ligado, que neste caso é o pulso 
		--enviado pelo pulse generator.
		elsif (en = '1') then
		   --Se tiver chegado ao ultimo endereço, recomeça a contagem.
			if (s_count = 255) then
				s_count <= 0;
			else
				s_count <= s_count + 1;
			end if;
		end if;
	end if;
	end process;
	--Como usamos um sinal, temos de dar o seu valor á variavel do output, neste caso AddressOut1,
	--mas fazendo as respetivas mudanças, uma vez que o sinal é do tipo "natural" e o output do tipo std_logic_vector.
	AddressOut <= std_logic_vector(to_unsigned(s_count, 8));
end behavioral;