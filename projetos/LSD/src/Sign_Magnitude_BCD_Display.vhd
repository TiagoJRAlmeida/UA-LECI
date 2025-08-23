library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.NUMERIC_STD.all;

entity Sign_Magnitude_BCD_Display is
	port(BinIn : in std_logic_vector(7 downto 0);
		  HEX1  : out std_logic_vector(6 downto 0);
		  HEX2  : out std_logic_vector(6 downto 0);
		  HEX3  : out std_logic_vector(6 downto 0);
		  HEX4  : out std_logic_vector(6 downto 0));
end Sign_Magnitude_BCD_Display;

	
architecture behavioral of Sign_Magnitude_BCD_Display is

	signal s_BCDOut1 : std_logic_vector(3 downto 0);
	signal s_BCDOut2 : std_logic_vector(3 downto 0);
	signal s_BCDOut3 : std_logic_vector(3 downto 0);
	signal s_BCDOut4 : std_logic_vector(3 downto 0);
	
begin
	
	--Este código serve para juntar o Bin2BCD e o Bin7SegDecoder, para que assim juntos,
   --consigam tranformar um numero binario de 8 bits em 4 numeros bcd de 4 bits cada,
	--que são enviados para os displays para aparecerem como números decimais.
	Bin2BCD : entity work.Bin2BCD(behavioral)
								port map(BinIn => BinIn,
											BCDOut1 => s_BCDOut1,
											BCDOut2 => s_BCDOut2,
											BCDOut3 => s_BCDOut3,
											BCDOut4 => s_BCDOut4);
		
											
	HEX_1 : entity work.Bin7SegDecoder(behavioral)
										port map(binInput =>  s_BCDOut1,
													decOut_n => HEX1);
													
	HEX_2 : entity work.Bin7SegDecoder(behavioral)
										port map(binInput =>  s_BCDOut2,
													decOut_n => HEX2);
													
	HEX_3 : entity work.Bin7SegDecoder(behavioral)
										port map(binInput =>  s_BCDOut3,
													decOut_n => HEX3);
													
	HEX_4 : entity work.Bin7SegDecoder(behavioral)
										port map(binInput => s_BCDOut4,
													decOut_n => HEX4);										
											
end behavioral;