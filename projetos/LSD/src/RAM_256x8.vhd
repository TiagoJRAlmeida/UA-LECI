library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity RAM_256x8 is
    port( writeClk, writeEnable : in std_logic;
          writeData : in  std_logic_vector(7 downto 0);
          address : in std_logic_vector(7 downto 0);
			 reset_ram : in std_logic;
          readData : out std_logic_vector(7 downto 0));
end RAM_256x8;

architecture behavioral of RAM_256x8 is
    --Criação de uma array de 256 endereços e que armazena palavras de 8 bits(Mesmas dimenções da rom).
    type TRam is array (0 to 255) of std_logic_vector(7 downto 0);
    signal s_memory : TRam;
    begin 
        process(writeClk)
        begin 
            if (rising_edge(writeClk)) then
	            --Caso o reset ram  ou o reset global, uma vez que este tambem ativa o reset ram,
					--seja ativado a memoria da ram é limpa, ou seja, todos os endereços recebem o valor 0.			
					if (reset_ram = '1') then
						s_memory <= (others=>(others => '0'));
					--Caso o enable esteja ativado, neste caso o output timerOut vindo do timer, 
					--a ram guarda no endereço recebido do AddressGenerator o resultado vindo da Arithmetic_Unit.
					--Escrita síncrona.
					elsif (writeEnable = '1') then
						s_memory(to_integer(unsigned(address))) <= writeData;
					end if;
            end if;
        end process;
		  --Leitura assíncrona
        readData <= s_memory(to_integer(unsigned(address)));
end behavioral;