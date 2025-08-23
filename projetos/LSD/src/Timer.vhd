library ieee;
use ieee.STD_LOGIC_1164.all;
use ieee.NUMERIC_STD.all;

entity Timer is
    generic(N : positive := 3);
    port(start : in std_logic;
         clk : in std_logic;
         timerOut : out std_logic);
end Timer;

architecture behavioral of Timer is
signal s_count : integer := 0;
begin 
    process(clk)
    begin 
        if (rising_edge(clk)) then
            if(s_count = 0) then
                if(start = '1') then
                    s_count <= s_count + 1;
                end if;
                timerOut <= '1';
            else
                if(s_count = N - 1)then
                    timerOut <= '1';
                    s_count <= 0;
                else
                    timerOut <= '0';
                    s_count <= s_count + 1;
                end if;
            end if;
        end if;
    end process;
end behavioral;