library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.NUMERIC_STD.all;

entity AddressGenerator is
	port(clk      	  : in std_logic;	
		  RESET_RAM   : in std_logic;
		  RST         : in std_logic;
		  en      	  : in std_logic;
		  Ram_AddrOut : out std_logic_vector(7 downto 0);
		  Rom_AddrOut : out std_logic_vector(7 downto 0));
end AddressGenerator;

architecture behavioral of AddressGenerator is
begin 
	 --Juntar as geração de endereços da ram e do rom em uma unica "peça"
	 --chamada AddressGenerator.
	 RamAddr : entity work.RamAddr(behavioral)
                        port map(clk => clk,
                                 RESET_RAM => RESET_RAM,
											AddressOut => Ram_AddrOut,
											en => en);

    RomAddr : entity work.RomAddr(behavioral)
                        port map(clk => clk,
											RST => RST,
											en => en,
                                 AddressOut1 => Rom_AddrOut );

end behavioral;