library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Arithmetic_Unit is
    port( Result : out std_logic_vector(7 downto 0);
	       Filter_on : in std_logic;
          Operand1,Operand2,Operand3 : in std_logic_vector(7 downto 0));
end Arithmetic_Unit;

architecture behavioral of Arithmetic_Unit is 
    signal s_result1, s_result2, s_result3 : std_logic_vector(7 downto 0);
begin
	 --Uso dos blocos Adder e Sub criados anteriormente para realizar a operação de filtragem.
	 --Neste caso, a operação necessita de 2 somas e 1 subtração, logo usaremos 2 adders e 1 sub.
    Adder1: entity work.Adder(behavioral)
                port map(operand1 => Operand1,
					          Filter_on => Filter_on,
                         operand2 => Operand3,
                         result => s_result1);
								 
    Adder2 : entity work.Adder(behavioral)
                port map(operand1 => Operand2,
                         operand2 => Operand2,
								 Filter_on => Filter_on,
                         result => s_result2);
									 
    Sub1 :   entity work.Sub(behavioral)
                port map(operand1 => s_result1,
                         operand2 => s_result2,
								 Filter_on => Filter_on,	 
                         result => s_result3);
    Result <= s_result3;
end behavioral;