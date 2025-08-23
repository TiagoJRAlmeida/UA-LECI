library ieee;
use ieee.std_logic_1164.all;

entity ControlUnit is
    port( clk,filter,reset_ram,reset,iniciate : in std_logic;
          start,filter_on,rst_ram,rst : out std_logic);
end ControlUnit;

architecture behavioral of ControlUnit is

    type TState is (STARTED,FILTERED_ON,RSTED_RAM,RSTED);
    signal s_cs,s_ns : TState;

begin 
	--Processo do reset. Caso ele seja ativo, o sistema levará reset, não interessa que estado é que está.
    sync_proc : process(clk)
    begin
        if (rising_edge(clk)) then 
            if(reset = '1') then
                s_cs <= RSTED;
            else
                s_cs <= s_ns;
            end if;
        end if;
    end process;

    comb_proc : process(s_cs,filter,reset_ram,iniciate,reset)
    begin 
        case(s_cs) is
		  --Caso esteja no estado RSTED, tudo volta ao inicio e só recomeça caso o iniciate seja ativado,
		  --indo assim para o estado STARTED.
        when RSTED => 
            rst <= '1';
            start <= '0';
            filter_on <= '0';
            rst_ram <= '1';
            if (iniciate = '1') then
                s_ns <= STARTED;
            else 
                s_ns <= RSTED;
            end if;
		  --Caso esteja no estado STARTED, a contagem começa, mostrando os valores da rom no display,
		  --sem realizar realizar operações, sendo que os displays da ram apenas mostram zeros.
        when STARTED =>
            start <= '1';
            rst <= '0';
            filter_on <= '0';
            rst_ram <= '0';
				if (filter = '1') then
					s_ns <= FILTERED_ON;
            elsif (reset_ram = '1') then
                s_ns <= RSTED_RAM;
            else
                s_ns <= STARTED;
            end if;
		   --Caso esteja no estado RSTED_RAM, a contagem da rom continua, com a diferença que todos os valores
			--guardados na ram até o momento são apagados.
         when RSTED_RAM =>
            rst_ram <= '1';
            rst <= '0';
            start <= '1';
            filter_on <= '0';
            if (filter = '1') then
                s_ns <= FILTERED_ON;
            else
                s_ns <= RSTED_RAM;
            end if;
			--Caso esteja no estado FILTERED_ON, a contagem da rom continua mas desta vez as operações de filtragem tambem
			--ocorrem, aparecendo o resultado nos displays. Caso o input filter, que na pratica é um switch, seja desligado,
			--este volta para o estado RSTED_RAM, onde os valores da rom continuam a aparecer mas as operações param.
         when FILTERED_ON =>
            filter_on <= '1';
            start <= '1';
            rst <= '0';
            rst_ram <= '0';
				if (filter  = '0') then
					s_ns <= RSTED_RAM;
            else 
                s_ns <= FILTERED_ON;
            end if;
        when others =>
            s_ns <= RSTED;
        end case;
    end process;
end behavioral;