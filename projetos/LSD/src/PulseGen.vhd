library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;

entity PulseGen is 
	--Valor variavel até qual o pulseGen conta antes de enviar um pulso.
	--Neste caso deve contar até 25 milhões para enviar um pulso de 2 em 2 segundos, 
	--ou seja, envia um pulso com uma frequencia de 2hz.
	generic(MAX   : positive := 25000000);
	port(clk 	  : in std_logic;
		  start    : in std_logic;
		  pulse : out std_logic);
end PulseGen;

architecture behavioral of PulseGen is	

	signal s_cnt : natural range 0 to MAX-1;
	
begin
	process(clk)
	begin 
		if rising_edge(clk) then
		--Apenas começa a contagem caso start esteja ativado.
			if start = '1' then
				pulse <= '0';
				s_cnt <= s_cnt + 1;
				--Caso tenho acabado a contagem, isto é tenha chegado ao valor determinado menos 1,
				--porque a contagem começa no 0, envia um pulso e recomeça a contagem.
				if s_cnt = MAX-1 then
					s_cnt <= 0;
					pulse <= '1';
				end if;
			end if;
		end if;
	end process;
end behavioral;