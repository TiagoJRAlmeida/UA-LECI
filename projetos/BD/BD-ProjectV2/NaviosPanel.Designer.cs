namespace BD_Final_Project
{
    partial class NaviosPanel
    {
        /// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            tabPage2 = new TabPage();
            splitContainer1 = new SplitContainer();
            label9 = new Label();
            label6 = new Label();
            SearchBy = new ComboBox();
            SortBy = new Label();
            sort = new ComboBox();
            EmpresaSearch = new TextBox();
            comboBox1 = new ComboBox();
            Apply = new Button();
            label10 = new Label();
            label7 = new Label();
            comboBox2 = new ComboBox();
            label8 = new Label();
            comboBox3 = new ComboBox();
            textBox4 = new TextBox();
            comboBox4 = new ComboBox();
            button6 = new Button();
            panel2 = new Panel();
            textBox6 = new TextBox();
            label12 = new Label();
            listBox2 = new ListBox();
            textBox5 = new TextBox();
            label11 = new Label();
            label5 = new Label();
            panel1 = new Panel();
            richTextBox1 = new RichTextBox();
            label4 = new Label();
            listBox1 = new ListBox();
            tabPage1 = new TabPage();
            ShowTrabalhadoresAssociados = new Button();
            TrabalhadorAdicionar = new Button();
            NavioEditar = new Button();
            NavioApagar = new Button();
            NavioAdicionar = new Button();
            label3 = new Label();
            label2 = new Label();
            label1 = new Label();
            NavioEmpresaNIF = new TextBox();
            NavioCapacidade = new TextBox();
            NavioNome = new TextBox();
            listBoxNavios = new ListBox();
            tabControl1 = new TabControl();
            tabPage2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).BeginInit();
            splitContainer1.Panel1.SuspendLayout();
            splitContainer1.Panel2.SuspendLayout();
            splitContainer1.SuspendLayout();
            panel2.SuspendLayout();
            panel1.SuspendLayout();
            tabPage1.SuspendLayout();
            tabControl1.SuspendLayout();
            SuspendLayout();
            // 
            // tabPage2
            // 
            tabPage2.BackColor = SystemColors.ActiveCaption;
            tabPage2.Controls.Add(splitContainer1);
            tabPage2.Controls.Add(panel2);
            tabPage2.Controls.Add(panel1);
            tabPage2.Controls.Add(listBox1);
            tabPage2.Location = new Point(4, 24);
            tabPage2.Name = "tabPage2";
            tabPage2.Padding = new Padding(3, 3, 3, 3);
            tabPage2.Size = new Size(1128, 444);
            tabPage2.TabIndex = 1;
            tabPage2.Text = "Detalhes";
            // 
            // splitContainer1
            // 
            splitContainer1.Location = new Point(17, 194);
            splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            splitContainer1.Panel1.BackColor = SystemColors.Control;
            splitContainer1.Panel1.Controls.Add(label9);
            splitContainer1.Panel1.Controls.Add(label6);
            splitContainer1.Panel1.Controls.Add(SearchBy);
            splitContainer1.Panel1.Controls.Add(SortBy);
            splitContainer1.Panel1.Controls.Add(sort);
            splitContainer1.Panel1.Controls.Add(EmpresaSearch);
            splitContainer1.Panel1.Controls.Add(comboBox1);
            splitContainer1.Panel1.Controls.Add(Apply);
            // 
            // splitContainer1.Panel2
            // 
            splitContainer1.Panel2.BackColor = SystemColors.Control;
            splitContainer1.Panel2.Controls.Add(label10);
            splitContainer1.Panel2.Controls.Add(label7);
            splitContainer1.Panel2.Controls.Add(comboBox2);
            splitContainer1.Panel2.Controls.Add(label8);
            splitContainer1.Panel2.Controls.Add(comboBox3);
            splitContainer1.Panel2.Controls.Add(textBox4);
            splitContainer1.Panel2.Controls.Add(comboBox4);
            splitContainer1.Panel2.Controls.Add(button6);
            splitContainer1.Size = new Size(610, 234);
            splitContainer1.SplitterDistance = 288;
            splitContainer1.TabIndex = 4;
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.BorderStyle = BorderStyle.FixedSingle;
            label9.Location = new Point(79, 21);
            label9.Name = "label9";
            label9.Size = new Size(121, 17);
            label9.TabIndex = 2;
            label9.Text = "Filtros para os Navios";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(9, 62);
            label6.Name = "label6";
            label6.Size = new Size(52, 15);
            label6.TabIndex = 25;
            label6.Text = "Procurar";
            // 
            // SearchBy
            // 
            SearchBy.FormattingEnabled = true;
            SearchBy.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            SearchBy.Location = new Point(153, 80);
            SearchBy.Name = "SearchBy";
            SearchBy.Size = new Size(121, 23);
            SearchBy.TabIndex = 26;
            // 
            // SortBy
            // 
            SortBy.AutoSize = true;
            SortBy.Location = new Point(9, 117);
            SortBy.Margin = new Padding(2, 0, 2, 0);
            SortBy.Name = "SortBy";
            SortBy.Size = new Size(37, 15);
            SortBy.TabIndex = 28;
            SortBy.Text = "Filtrar";
            // 
            // sort
            // 
            sort.FormattingEnabled = true;
            sort.Items.AddRange(new object[] { "Crescente", "Decrescente" });
            sort.Location = new Point(152, 135);
            sort.Margin = new Padding(2, 2, 2, 2);
            sort.Name = "sort";
            sort.Size = new Size(122, 23);
            sort.TabIndex = 30;
            // 
            // EmpresaSearch
            // 
            EmpresaSearch.Location = new Point(9, 80);
            EmpresaSearch.Name = "EmpresaSearch";
            EmpresaSearch.Size = new Size(138, 23);
            EmpresaSearch.TabIndex = 24;
            // 
            // comboBox1
            // 
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            comboBox1.Location = new Point(8, 135);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(139, 23);
            comboBox1.TabIndex = 29;
            // 
            // Apply
            // 
            Apply.Location = new Point(70, 177);
            Apply.Margin = new Padding(2, 2, 2, 2);
            Apply.Name = "Apply";
            Apply.Size = new Size(139, 37);
            Apply.TabIndex = 27;
            Apply.Text = "Confirmar";
            Apply.UseVisualStyleBackColor = true;
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.BorderStyle = BorderStyle.FixedSingle;
            label10.Location = new Point(73, 21);
            label10.Name = "label10";
            label10.Size = new Size(158, 17);
            label10.TabIndex = 31;
            label10.Text = "Filtros para os Trabalhadores";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(23, 62);
            label7.Name = "label7";
            label7.Size = new Size(52, 15);
            label7.TabIndex = 32;
            label7.Text = "Procurar";
            // 
            // comboBox2
            // 
            comboBox2.FormattingEnabled = true;
            comboBox2.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            comboBox2.Location = new Point(167, 80);
            comboBox2.Name = "comboBox2";
            comboBox2.Size = new Size(121, 23);
            comboBox2.TabIndex = 33;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Location = new Point(23, 117);
            label8.Margin = new Padding(2, 0, 2, 0);
            label8.Name = "label8";
            label8.Size = new Size(37, 15);
            label8.TabIndex = 35;
            label8.Text = "Filtrar";
            // 
            // comboBox3
            // 
            comboBox3.FormattingEnabled = true;
            comboBox3.Items.AddRange(new object[] { "Crescente", "Decrescente" });
            comboBox3.Location = new Point(166, 135);
            comboBox3.Margin = new Padding(2, 2, 2, 2);
            comboBox3.Name = "comboBox3";
            comboBox3.Size = new Size(122, 23);
            comboBox3.TabIndex = 37;
            // 
            // textBox4
            // 
            textBox4.Location = new Point(23, 80);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(138, 23);
            textBox4.TabIndex = 31;
            // 
            // comboBox4
            // 
            comboBox4.FormattingEnabled = true;
            comboBox4.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            comboBox4.Location = new Point(22, 135);
            comboBox4.Name = "comboBox4";
            comboBox4.Size = new Size(139, 23);
            comboBox4.TabIndex = 36;
            // 
            // button6
            // 
            button6.Location = new Point(92, 177);
            button6.Margin = new Padding(2, 2, 2, 2);
            button6.Name = "button6";
            button6.Size = new Size(139, 37);
            button6.TabIndex = 34;
            button6.Text = "Confirmar";
            button6.UseVisualStyleBackColor = true;
            // 
            // panel2
            // 
            panel2.BackColor = SystemColors.ButtonFace;
            panel2.BorderStyle = BorderStyle.FixedSingle;
            panel2.Controls.Add(textBox6);
            panel2.Controls.Add(label12);
            panel2.Controls.Add(listBox2);
            panel2.Controls.Add(textBox5);
            panel2.Controls.Add(label11);
            panel2.Controls.Add(label5);
            panel2.Location = new Point(678, 165);
            panel2.Name = "panel2";
            panel2.Size = new Size(419, 263);
            panel2.TabIndex = 3;
            // 
            // textBox6
            // 
            textBox6.Location = new Point(110, 76);
            textBox6.Name = "textBox6";
            textBox6.Size = new Size(177, 23);
            textBox6.TabIndex = 42;
            // 
            // label12
            // 
            label12.AutoSize = true;
            label12.Location = new Point(19, 79);
            label12.Name = "label12";
            label12.Size = new Size(85, 15);
            label12.TabIndex = 41;
            label12.Text = "Salário Médio: ";
            // 
            // listBox2
            // 
            listBox2.FormattingEnabled = true;
            listBox2.ItemHeight = 15;
            listBox2.Location = new Point(19, 118);
            listBox2.Name = "listBox2";
            listBox2.Size = new Size(372, 124);
            listBox2.TabIndex = 40;
            // 
            // textBox5
            // 
            textBox5.Location = new Point(192, 46);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(177, 23);
            textBox5.TabIndex = 39;
            // 
            // label11
            // 
            label11.AutoSize = true;
            label11.Location = new Point(19, 51);
            label11.Name = "label11";
            label11.Size = new Size(167, 15);
            label11.TabIndex = 38;
            label11.Text = "Quantidade de Trabalhadores: ";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.BorderStyle = BorderStyle.FixedSingle;
            label5.Location = new Point(116, 10);
            label5.Name = "label5";
            label5.Size = new Size(194, 17);
            label5.TabIndex = 0;
            label5.Text = "Informação Sobre os Trabalhadores";
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.ButtonFace;
            panel1.BorderStyle = BorderStyle.FixedSingle;
            panel1.Controls.Add(richTextBox1);
            panel1.Controls.Add(label4);
            panel1.Location = new Point(678, 19);
            panel1.Name = "panel1";
            panel1.Size = new Size(419, 140);
            panel1.TabIndex = 2;
            // 
            // richTextBox1
            // 
            richTextBox1.Location = new Point(54, 39);
            richTextBox1.Name = "richTextBox1";
            richTextBox1.ReadOnly = true;
            richTextBox1.Size = new Size(315, 86);
            richTextBox1.TabIndex = 1;
            richTextBox1.Text = "";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.BorderStyle = BorderStyle.FixedSingle;
            label4.Location = new Point(135, 13);
            label4.Name = "label4";
            label4.Size = new Size(160, 17);
            label4.TabIndex = 0;
            label4.Text = "Informação Sobre a Empresa";
            // 
            // listBox1
            // 
            listBox1.FormattingEnabled = true;
            listBox1.ItemHeight = 15;
            listBox1.Location = new Point(17, 19);
            listBox1.Name = "listBox1";
            listBox1.Size = new Size(610, 169);
            listBox1.TabIndex = 1;
            // 
            // tabPage1
            // 
            tabPage1.BackColor = SystemColors.ActiveCaption;
            tabPage1.Controls.Add(ShowTrabalhadoresAssociados);
            tabPage1.Controls.Add(TrabalhadorAdicionar);
            tabPage1.Controls.Add(NavioEditar);
            tabPage1.Controls.Add(NavioApagar);
            tabPage1.Controls.Add(NavioAdicionar);
            tabPage1.Controls.Add(label3);
            tabPage1.Controls.Add(label2);
            tabPage1.Controls.Add(label1);
            tabPage1.Controls.Add(NavioEmpresaNIF);
            tabPage1.Controls.Add(NavioCapacidade);
            tabPage1.Controls.Add(NavioNome);
            tabPage1.Controls.Add(listBoxNavios);
            tabPage1.ForeColor = SystemColors.ActiveCaptionText;
            tabPage1.Location = new Point(4, 24);
            tabPage1.Name = "tabPage1";
            tabPage1.Padding = new Padding(3, 3, 3, 3);
            tabPage1.Size = new Size(1128, 444);
            tabPage1.TabIndex = 0;
            tabPage1.Text = "Gerir Navios";
            // 
            // ShowTrabalhadoresAssociados
            // 
            ShowTrabalhadoresAssociados.Location = new Point(535, 361);
            ShowTrabalhadoresAssociados.Name = "ShowTrabalhadoresAssociados";
            ShowTrabalhadoresAssociados.Size = new Size(166, 58);
            ShowTrabalhadoresAssociados.TabIndex = 11;
            ShowTrabalhadoresAssociados.Text = "Trabalhadores Associados";
            ShowTrabalhadoresAssociados.UseVisualStyleBackColor = true;
            ShowTrabalhadoresAssociados.Click += ShowTrabalhadoresAssociados_Click;
            // 
            // TrabalhadorAdicionar
            // 
            TrabalhadorAdicionar.Location = new Point(707, 361);
            TrabalhadorAdicionar.Name = "TrabalhadorAdicionar";
            TrabalhadorAdicionar.Size = new Size(166, 58);
            TrabalhadorAdicionar.TabIndex = 10;
            TrabalhadorAdicionar.Text = "Adicionar Trabalhador";
            TrabalhadorAdicionar.UseVisualStyleBackColor = true;
            // 
            // NavioEditar
            // 
            NavioEditar.Location = new Point(363, 361);
            NavioEditar.Name = "NavioEditar";
            NavioEditar.Size = new Size(166, 58);
            NavioEditar.TabIndex = 9;
            NavioEditar.Text = "Editar Navio";
            NavioEditar.UseVisualStyleBackColor = true;
            NavioEditar.Click += NavioEditar_Click;
            // 
            // NavioApagar
            // 
            NavioApagar.Location = new Point(191, 361);
            NavioApagar.Name = "NavioApagar";
            NavioApagar.Size = new Size(166, 58);
            NavioApagar.TabIndex = 8;
            NavioApagar.Text = "Apagar Navio";
            NavioApagar.UseVisualStyleBackColor = true;
            NavioApagar.Click += NavioApagar_Click;
            // 
            // NavioAdicionar
            // 
            NavioAdicionar.Location = new Point(19, 361);
            NavioAdicionar.Name = "NavioAdicionar";
            NavioAdicionar.Size = new Size(166, 58);
            NavioAdicionar.TabIndex = 7;
            NavioAdicionar.Text = "Adicionar Navio";
            NavioAdicionar.UseVisualStyleBackColor = true;
            NavioAdicionar.Click += NavioAdicionar_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(752, 195);
            label3.Name = "label3";
            label3.Size = new Size(171, 15);
            label3.TabIndex = 6;
            label3.Text = "NIF da Empresa Dona do Navio";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(752, 129);
            label2.Name = "label2";
            label2.Size = new Size(166, 15);
            label2.TabIndex = 5;
            label2.Text = "Capacidade Máxima do Navio";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(752, 63);
            label1.Name = "label1";
            label1.Size = new Size(91, 15);
            label1.TabIndex = 4;
            label1.Text = "Nome do Navio";
            // 
            // NavioEmpresaNIF
            // 
            NavioEmpresaNIF.Location = new Point(752, 213);
            NavioEmpresaNIF.Name = "NavioEmpresaNIF";
            NavioEmpresaNIF.Size = new Size(166, 23);
            NavioEmpresaNIF.TabIndex = 3;
            // 
            // NavioCapacidade
            // 
            NavioCapacidade.Location = new Point(752, 147);
            NavioCapacidade.Name = "NavioCapacidade";
            NavioCapacidade.Size = new Size(166, 23);
            NavioCapacidade.TabIndex = 2;
            // 
            // NavioNome
            // 
            NavioNome.Location = new Point(752, 81);
            NavioNome.Name = "NavioNome";
            NavioNome.Size = new Size(166, 23);
            NavioNome.TabIndex = 1;
            // 
            // listBoxNavios
            // 
            listBoxNavios.FormattingEnabled = true;
            listBoxNavios.ItemHeight = 15;
            listBoxNavios.Location = new Point(19, 17);
            listBoxNavios.Name = "listBoxNavios";
            listBoxNavios.Size = new Size(622, 304);
            listBoxNavios.TabIndex = 0;
            listBoxNavios.SelectedIndexChanged += listBoxNavios_SelectedIndexChanged;
            // 
            // tabControl1
            // 
            tabControl1.Controls.Add(tabPage1);
            tabControl1.Controls.Add(tabPage2);
            tabControl1.Location = new Point(3, 3);
            tabControl1.Name = "tabControl1";
            tabControl1.SelectedIndex = 0;
            tabControl1.Size = new Size(1136, 472);
            tabControl1.TabIndex = 0;
            // 
            // NaviosPanel
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(tabControl1);
            Name = "NaviosPanel";
            Size = new Size(1139, 478);
            Load += NaviosPanel_Load;
            tabPage2.ResumeLayout(false);
            splitContainer1.Panel1.ResumeLayout(false);
            splitContainer1.Panel1.PerformLayout();
            splitContainer1.Panel2.ResumeLayout(false);
            splitContainer1.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)splitContainer1).EndInit();
            splitContainer1.ResumeLayout(false);
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            tabPage1.ResumeLayout(false);
            tabPage1.PerformLayout();
            tabControl1.ResumeLayout(false);
            ResumeLayout(false);
        }

        #endregion

        private TabPage tabPage2;
        private SplitContainer splitContainer1;
        private Label label9;
        private Label label6;
        private ComboBox SearchBy;
        private Label SortBy;
        private ComboBox sort;
        private TextBox EmpresaSearch;
        private ComboBox comboBox1;
        private Button Apply;
        private Label label10;
        private Label label7;
        private ComboBox comboBox2;
        private Label label8;
        private ComboBox comboBox3;
        private TextBox textBox4;
        private ComboBox comboBox4;
        private Button button6;
        private Panel panel2;
        private TextBox textBox6;
        private Label label12;
        private ListBox listBox2;
        private TextBox textBox5;
        private Label label11;
        private Label label5;
        private Panel panel1;
        private RichTextBox richTextBox1;
        private Label label4;
        private ListBox listBox1;
        private TabPage tabPage1;
        private Button ShowTrabalhadoresAssociados;
        private Button TrabalhadorAdicionar;
        private Button NavioEditar;
        private Button NavioApagar;
        private Button NavioAdicionar;
        private Label label3;
        private Label label2;
        private Label label1;
        public TextBox NavioEmpresaNIF;
        private TextBox NavioCapacidade;
        private TextBox NavioNome;
        private ListBox listBoxNavios;
        private TabControl tabControl1;
    }
}
