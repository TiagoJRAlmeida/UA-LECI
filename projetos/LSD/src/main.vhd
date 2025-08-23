library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.NUMERIC_STD.all;

entity main is
	port(CLOCK_50  : in std_logic;
		  KEY 		: in std_logic_vector(2 downto 0);
		  SW        : in std_logic_vector(0 downto 0);
		  HEX0      : out std_logic_vector(6 downto 0);
		  HEX1      : out std_logic_vector(6 downto 0);
		  HEX2      : out std_logic_vector(6 downto 0);
		  HEX3      : out std_logic_vector(6 downto 0);
		  HEX4      : out std_logic_vector(6 downto 0);
		  HEX5      : out std_logic_vector(6 downto 0);
		  HEX6      : out std_logic_vector(6 downto 0);
		  HEX7      : out std_logic_vector(6 downto 0));
end main;

architecture behavioral of main is
	
	signal s_pulse : std_logic;
	signal s_Rom_AddrOut : std_logic_vector(7 downto 0);
	signal s_Ram_AddrOut : std_logic_vector(7 downto 0);
	signal s_Rom_dataOut : std_logic_vector(7 downto 0);
	signal s_Ram_dataOut : std_logic_vector(7 downto 0);
	signal s_op1 : std_logic_vector(7 downto 0);
	signal s_op2 : std_logic_vector(7 downto 0);
	signal s_op3 : std_logic_vector(7 downto 0);
	signal s_result : std_logic_vector(7 downto 0);
	signal s_timerOut : std_logic;
	signal s_start : std_logic;
	signal s_filter_on : std_logic;
	signal s_rst : std_logic;
	signal s_rst_ram : std_logic;
	signal s_KEY0 : std_logic;
	signal s_KEY1 : std_logic;
	signal s_KEY2 : std_logic;
	
begin 
	 --Este código server para juntar todas as "peças" anteriores de forma a criar um circuito que funcione.
	 PulseGen : entity work.PulseGen(behavioral)
								port map(clk => CLOCK_50,
											start => s_start,
											pulse => s_pulse);
											
	 Timer : entity work.Timer(behavioral)
							port map(clk => CLOCK_50,
										start => s_pulse,
										timerOut => s_timerOut);
											
	 AddressGen : entity work.AddressGenerator(behavioral)
									port map(clk => CLOCK_50,
												RESET_RAM => s_rst_ram,
												RST => s_rst,
												en => s_pulse,
												Rom_AddrOut => s_Rom_AddrOut,
												Ram_AddrOut => s_Ram_AddrOut);
												
	 Rom : entity work.TriangSignal_ROM_256x8(Behavioral)
						port map(address => s_rom_addrOut,
									dataOut => s_Rom_dataOut);
									
	 DelayLine : entity work.DelayLine(behavioral)
								port map(clk => CLOCK_50,   
										   WrData => s_Rom_dataOut,    
										   WE => s_pulse,        
										   RST => s_rst,
										   DataOut1 => s_op1,   
										   DataOut2 => s_op2, 
											DataOut3 => s_op3);
											
											
	 ArithmeticUnit : entity work.Arithmetic_Unit(behavioral)
										port map(Operand1 => s_op1, --k+1
													Operand2 => s_op2, --k
													Operand3 => s_op3, --k-1
													Filter_on => s_filter_on,
													result => s_result);
													
													
	 Ram : entity work.RAM_256x8(behavioral)
						 port map(writeClk => CLOCK_50, 
									 writeEnable => s_timerOut,
									 writeData => s_result,
									 reset_ram => s_rst_ram,
									 address => s_Ram_AddrOut,
									 readData => s_Ram_dataOut);
									 
	 ControlUnit : entity work.ControlUnit(behavioral)
									port map(clk => CLOCK_50,
									         filter => SW(0),
												reset_ram => s_KEY1,
												reset => s_KEY2,
												iniciate => s_KEY0,
												start => s_start,
												filter_on => s_filter_on,
												rst_ram => s_rst_ram,
												rst => s_rst);
									 
    Rom_BCDDisplay : entity work.Sign_Magnitude_BCD_Display(behavioral)
									port map(BinIn => s_Rom_dataOut,
												HEX1 => HEX0,
												HEX2 => HEX1,
												HEX3 => HEX2,
												HEX4 => HEX3);
												
	 Ram_BCDDisplay : entity work.Sign_Magnitude_BCD_Display(behavioral)
									port map(BinIn => s_Ram_dataOut,
												HEX1 => HEX4,
												HEX2 => HEX5,
												HEX3 => HEX6,
												HEX4 => HEX7);
	 
	 Debouncer_Key0 : entity work.Debouncer(Behavioral)
										port map(refClk => CLOCK_50,
													dirtyIn => not KEY(0),
													pulsedOut => s_KEY0);	
													
	 Debouncer_Key1 : entity work.Debouncer(Behavioral)
										port map(refClk => CLOCK_50,
													dirtyIn => not KEY(1),
													pulsedOut => s_KEY1);
													
	 Debouncer_Key2 : entity work.Debouncer(Behavioral)
										port map(refClk => CLOCK_50,
													dirtyIn => not KEY(2),
													pulsedOut => s_KEY2);										
													
	 

end behavioral;