library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity Bin2BCD is
port(BinIn   : in std_logic_vector(7 downto 0);
	  BCDOut1 : out std_logic_vector(3 downto 0);
	  BCDOut2 : out std_logic_vector(3 downto 0);
	  BCDOut3 : out std_logic_vector(3 downto 0);
	  BCDOut4 : out std_logic_vector(3 downto 0));
end Bin2BCD;

architecture behavioral of Bin2BCD is 
	
		signal s_BinIn : Integer;
		signal s_BinIn_decimal : Integer;
		signal s_BCDOut3 : Integer;
		signal s_BCDOut2 : Integer;
		signal s_BCDOut1 : Integer;
		
begin 
	process(BinIn, s_BinIn, s_BinIn_decimal)
	begin
		s_BinIn <= to_integer(signed(BinIn));
		s_BinIn_decimal <= s_BinIn - 100;
		--Tratar da saida BCDOut4 em primeiro lugar
		if (BinIn(7) = '1') then
			BCDOut4 <= "1010";
			s_BinIn <= to_integer(signed(BinIn)) * (-1);
		else
			BCDOut4 <= "0000";
		end if;
		
		--Tratar das saidas BCDOut3, BCDOut2, BCDOut1 quando BinIn > 100 em segundo lugar
		if (s_BinIn > 100) then
			s_BCDOut3 <= s_BinIn / 100;
			s_BCDOut2 <= s_BinIn_decimal / 10;
			s_BCDOut1 <= s_BinIn_decimal rem 10;
		
		--Tratar das saidas BCDOut3, BCDOut2, BCDOut1 quando 10 < BinIn < 100 em terceiro lugar
		elsif (s_BinIn > 10)then 
			s_BCDOut3 <= 0;
			s_BCDOut2 <= s_BinIn / 10;
			s_BCDOut1 <= s_BinIn rem 10;
			
		--Tratar das saidas BCDOut3, BCDOut2, BCDOut1 quando 0 < BinIn < 10 em ultimo lugar	
		else
			s_BCDOut3 <= 0;
			s_BCDOut2 <= 0;
			s_BCDOut1 <= s_BinIn;
		end if;
	end process;
	BCDOut1 <= std_logic_vector(to_unsigned(s_BCDOut1 ,4));
	BCDOut2 <= std_logic_vector(to_unsigned(s_BCDOut2 ,4));
	BCDOut3 <= std_logic_vector(to_unsigned(s_BCDOut3 ,4));
end behavioral;