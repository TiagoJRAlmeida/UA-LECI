library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity Bin7SegDecoder is
	port(binInput : in std_logic_vector(3 downto 0);
		  decOut_n : out std_logic_vector(6 downto 0));
end Bin7SegDecoder;

architecture behavioral of Bin7SegDecoder is
begin
	--Dependendo do input que receber este dá output ao
	--valor binário que ligue o display de 7 segmentos de forma a formar esse numero em decimal,
	--com a exceção do número 10, que caso esse seja o input, o valor que sairá para fora formará um "-",
	--e de valores maiores que 10 e menores a 0, que nesse caso será um erro e o display formará um "0".
	decOut_n <= "1111001" when (binInput = "0001") else --1
					"0100100" when (binInput = "0010") else --2  
					"0110000" when (binInput = "0011") else --3  
					"0011001" when (binInput = "0100") else --4
					"0010010" when (binInput = "0101") else --5
					"0000010" when (binInput = "0110") else --6
					"1111000" when (binInput = "0111") else --7
					"0000000" when (binInput = "1000") else --8
					"0010000" when (binInput = "1001") else --9
					"0111111" when (binInput = "1010") else --10 => -
					"1000000"; --0
end behavioral;