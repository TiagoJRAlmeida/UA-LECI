library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Sub is
    port( operand1 : in std_logic_vector(7 downto 0);
          operand2 : in std_logic_vector(7 downto 0);
			 Filter_on : in std_logic;
          result : out std_logic_vector(7 downto 0));
end Sub;

architecture behavioral of Sub is
 signal s_operand1, s_operand2, s_result : signed(7 downto 0);
begin
	s_operand1 <= signed(operand1);
	s_operand2 <= signed(operand2);
	process(Filter_on, s_operand1, s_operand2)
	begin
	
	   --Se o filtro estiver ligado, realiza a operação de soma, caso contrário, o resultado 
		--é dito como 0, uma vez que o processo de filtragem não está ativado e as contas não devem ser realizadas.
		 if Filter_on = '1' then 
			s_result <= s_operand1 - s_operand2;
		 else
			s_result <= (others => '0');
		 end if;
	end process;

   result <= std_logic_vector(s_result);
end behavioral;