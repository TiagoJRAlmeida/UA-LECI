namespace BD_Final_Project
{
    partial class EmpresasPanel
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
            panel1 = new Panel();
            ShowNaviosButton = new Button();
            listBoxEmpresas = new ListBox();
            label6 = new Label();
            SearchBy = new ComboBox();
            SortBy = new Label();
            sort = new ComboBox();
            EmpresaSearch = new TextBox();
            label1 = new Label();
            comboBox1 = new ComboBox();
            EmpresaNome = new TextBox();
            EmpresaAdicionar = new Button();
            Apply = new Button();
            EmpresaApagar = new Button();
            EmpresaEditar = new Button();
            EmpresaNIF = new TextBox();
            label5 = new Label();
            label4 = new Label();
            EmpresaEmail = new TextBox();
            EmpresaEndereco = new TextBox();
            label3 = new Label();
            EmpresaTelefone = new TextBox();
            label2 = new Label();
            NavioAdicionar = new Button();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.ActiveCaption;
            panel1.Controls.Add(NavioAdicionar);
            panel1.Controls.Add(ShowNaviosButton);
            panel1.Controls.Add(listBoxEmpresas);
            panel1.Controls.Add(label6);
            panel1.Controls.Add(SearchBy);
            panel1.Controls.Add(SortBy);
            panel1.Controls.Add(sort);
            panel1.Controls.Add(EmpresaSearch);
            panel1.Controls.Add(label1);
            panel1.Controls.Add(comboBox1);
            panel1.Controls.Add(EmpresaNome);
            panel1.Controls.Add(EmpresaAdicionar);
            panel1.Controls.Add(Apply);
            panel1.Controls.Add(EmpresaApagar);
            panel1.Controls.Add(EmpresaEditar);
            panel1.Controls.Add(EmpresaNIF);
            panel1.Controls.Add(label5);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(EmpresaEmail);
            panel1.Controls.Add(EmpresaEndereco);
            panel1.Controls.Add(label3);
            panel1.Controls.Add(EmpresaTelefone);
            panel1.Controls.Add(label2);
            panel1.Location = new Point(3, 3);
            panel1.Name = "panel1";
            panel1.Size = new Size(1132, 470);
            panel1.TabIndex = 26;
            // 
            // ShowNaviosButton
            // 
            ShowNaviosButton.Location = new Point(490, 375);
            ShowNaviosButton.Name = "ShowNaviosButton";
            ShowNaviosButton.Size = new Size(146, 62);
            ShowNaviosButton.TabIndex = 24;
            ShowNaviosButton.Text = "Navios Associados";
            ShowNaviosButton.UseVisualStyleBackColor = true;
            ShowNaviosButton.Click += ShowNaviosButton_Click;
            // 
            // listBoxEmpresas
            // 
            listBoxEmpresas.FormattingEnabled = true;
            listBoxEmpresas.ItemHeight = 15;
            listBoxEmpresas.Location = new Point(34, 14);
            listBoxEmpresas.Name = "listBoxEmpresas";
            listBoxEmpresas.Size = new Size(637, 274);
            listBoxEmpresas.TabIndex = 1;
            listBoxEmpresas.SelectedIndexChanged += listBoxEmpresas_SelectedIndexChanged;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(712, 14);
            label6.Name = "label6";
            label6.Size = new Size(52, 15);
            label6.TabIndex = 17;
            label6.Text = "Procurar";
            // 
            // SearchBy
            // 
            SearchBy.FormattingEnabled = true;
            SearchBy.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            SearchBy.Location = new Point(893, 42);
            SearchBy.Name = "SearchBy";
            SearchBy.Size = new Size(121, 23);
            SearchBy.TabIndex = 18;
            // 
            // SortBy
            // 
            SortBy.AutoSize = true;
            SortBy.Location = new Point(712, 107);
            SortBy.Margin = new Padding(2, 0, 2, 0);
            SortBy.Name = "SortBy";
            SortBy.Size = new Size(37, 15);
            SortBy.TabIndex = 21;
            SortBy.Text = "Filtrar";
            // 
            // sort
            // 
            sort.FormattingEnabled = true;
            sort.Items.AddRange(new object[] { "Crescente", "Decrescente" });
            sort.Location = new Point(850, 136);
            sort.Margin = new Padding(2);
            sort.Name = "sort";
            sort.Size = new Size(129, 23);
            sort.TabIndex = 23;
            // 
            // EmpresaSearch
            // 
            EmpresaSearch.Location = new Point(712, 42);
            EmpresaSearch.Name = "EmpresaSearch";
            EmpresaSearch.Size = new Size(175, 23);
            EmpresaSearch.TabIndex = 16;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(34, 317);
            label1.Name = "label1";
            label1.Size = new Size(104, 15);
            label1.TabIndex = 9;
            label1.Text = "Nome da Empresa";
            // 
            // comboBox1
            // 
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "Nome", "NIF", "Endereço", "Telefone", "Email", "---" });
            comboBox1.Location = new Point(712, 136);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(121, 23);
            comboBox1.TabIndex = 22;
            // 
            // EmpresaNome
            // 
            EmpresaNome.Location = new Point(34, 335);
            EmpresaNome.Name = "EmpresaNome";
            EmpresaNome.Size = new Size(175, 23);
            EmpresaNome.TabIndex = 3;
            // 
            // EmpresaAdicionar
            // 
            EmpresaAdicionar.Location = new Point(34, 375);
            EmpresaAdicionar.Name = "EmpresaAdicionar";
            EmpresaAdicionar.Size = new Size(146, 62);
            EmpresaAdicionar.TabIndex = 8;
            EmpresaAdicionar.Text = "Adicionar Empresa";
            EmpresaAdicionar.UseVisualStyleBackColor = true;
            EmpresaAdicionar.Click += AddEmpresaButton_Click;
            // 
            // Apply
            // 
            Apply.Location = new Point(712, 251);
            Apply.Margin = new Padding(2);
            Apply.Name = "Apply";
            Apply.Size = new Size(95, 37);
            Apply.TabIndex = 20;
            Apply.Text = "Confirmar";
            Apply.UseVisualStyleBackColor = true;
            Apply.Click += Apply_Click;
            // 
            // EmpresaApagar
            // 
            EmpresaApagar.Location = new Point(186, 375);
            EmpresaApagar.Name = "EmpresaApagar";
            EmpresaApagar.Size = new Size(146, 62);
            EmpresaApagar.TabIndex = 14;
            EmpresaApagar.Text = "Apagar Empresa";
            EmpresaApagar.UseVisualStyleBackColor = true;
            EmpresaApagar.Click += EmpresaApagar_Click;
            // 
            // EmpresaEditar
            // 
            EmpresaEditar.Location = new Point(338, 375);
            EmpresaEditar.Name = "EmpresaEditar";
            EmpresaEditar.Size = new Size(146, 62);
            EmpresaEditar.TabIndex = 15;
            EmpresaEditar.Text = "Editar Empresa";
            EmpresaEditar.UseVisualStyleBackColor = true;
            EmpresaEditar.Click += EmpresaEditar_Click;
            // 
            // EmpresaNIF
            // 
            EmpresaNIF.Location = new Point(259, 335);
            EmpresaNIF.Name = "EmpresaNIF";
            EmpresaNIF.Size = new Size(175, 23);
            EmpresaNIF.TabIndex = 4;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(259, 317);
            label5.Name = "label5";
            label5.Size = new Size(89, 15);
            label5.TabIndex = 13;
            label5.Text = "NIF da Empresa";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(936, 317);
            label4.Name = "label4";
            label4.Size = new Size(100, 15);
            label4.TabIndex = 12;
            label4.Text = "Email da Empresa";
            // 
            // EmpresaEmail
            // 
            EmpresaEmail.Location = new Point(936, 335);
            EmpresaEmail.Name = "EmpresaEmail";
            EmpresaEmail.Size = new Size(175, 23);
            EmpresaEmail.TabIndex = 7;
            // 
            // EmpresaEndereco
            // 
            EmpresaEndereco.Location = new Point(490, 335);
            EmpresaEndereco.Name = "EmpresaEndereco";
            EmpresaEndereco.Size = new Size(175, 23);
            EmpresaEndereco.TabIndex = 5;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(718, 317);
            label3.Name = "label3";
            label3.Size = new Size(115, 15);
            label3.TabIndex = 11;
            label3.Text = "Telefone da Empresa";
            // 
            // EmpresaTelefone
            // 
            EmpresaTelefone.Location = new Point(712, 335);
            EmpresaTelefone.Name = "EmpresaTelefone";
            EmpresaTelefone.Size = new Size(175, 23);
            EmpresaTelefone.TabIndex = 6;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(490, 317);
            label2.Name = "label2";
            label2.Size = new Size(120, 15);
            label2.TabIndex = 10;
            label2.Text = "Endereço da Empresa";
            // 
            // NavioAdicionar
            // 
            NavioAdicionar.Location = new Point(642, 375);
            NavioAdicionar.Name = "NavioAdicionar";
            NavioAdicionar.Size = new Size(146, 62);
            NavioAdicionar.TabIndex = 25;
            NavioAdicionar.Text = "Adicionar Navio";
            NavioAdicionar.UseVisualStyleBackColor = true;
            NavioAdicionar.Click += NavioAdicionar_Click;
            // 
            // EmpresasPanel
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(panel1);
            Name = "EmpresasPanel";
            Size = new Size(1139, 478);
            Load += EmpresasPanel_Load;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private ListBox listBoxEmpresas;
        private Label label6;
        private ComboBox SearchBy;
        private Label SortBy;
        private ComboBox sort;
        private TextBox EmpresaSearch;
        private Label label1;
        private ComboBox comboBox1;
        private TextBox EmpresaNome;
        private Button EmpresaAdicionar;
        private Button Apply;
        private Button EmpresaApagar;
        private Button EmpresaEditar;
        private TextBox EmpresaNIF;
        private Label label5;
        private Label label4;
        private TextBox EmpresaEmail;
        private TextBox EmpresaEndereco;
        private Label label3;
        private TextBox EmpresaTelefone;
        private Label label2;
        private Button ShowNaviosButton;
        private Button NavioAdicionar;
    }
}
