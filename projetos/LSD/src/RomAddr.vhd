library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.NUMERIC_STD.all;

entity RomAddr is
	port(clk        : in std_logic;	
		  en         : in std_logic;
		  RST        : in std_logic;
		  AddressOut1 : out std_logic_vector(7 downto 0));
end RomAddr;

architecture behavioral of RomAddr is

	signal s_count1 : natural := 0;

begin 
	process(clk)
	begin
		if rising_edge(clk) then
			--Se o reset global for ativado a criação de endereços recomeça do 0.
			if (RST = '1') then
				s_count1 <= 0;
			--Apenas cria os endereços caso o enable esteja ligado, que neste caso é o pulso 
			--enviado pelo pulse generator.
			elsif (en = '1') then
				--Se tiver chegado ao ultimo endereço, recomeça a contagem.
				if (s_count1 = 255) then
					s_count1 <= 0;
				else
					s_count1 <= s_count1 + 1;
				end if;
			end if;
		end if;
	end process;
	--Como usamos um sinal, temos de dar o seu valor á variavel do output, neste caso AddressOut1,
	--mas fazendo as respetivas mudanças, uma vez que o sinal é do tipo "natural" e o output do tipo std_logic_vector.
	AddressOut1 <= std_logic_vector(to_unsigned(s_count1, 8));
end behavioral;