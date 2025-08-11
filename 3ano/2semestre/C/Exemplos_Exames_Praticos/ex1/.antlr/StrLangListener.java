// Generated from /home/tiago/github/UA-LECI/3ano/2semestre/C/Exemplos_Exames_Praticos/ex1/StrLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link StrLangParser}.
 */
public interface StrLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link StrLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(StrLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link StrLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(StrLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by the {@code statPrint}
	 * labeled alternative in {@link StrLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatPrint(StrLangParser.StatPrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code statPrint}
	 * labeled alternative in {@link StrLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatPrint(StrLangParser.StatPrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code statAssign}
	 * labeled alternative in {@link StrLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatAssign(StrLangParser.StatAssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code statAssign}
	 * labeled alternative in {@link StrLangParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatAssign(StrLangParser.StatAssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableString}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableString(StrLangParser.PrintableStringContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableString}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableString(StrLangParser.PrintableStringContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableSubstitution}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableSubstitution(StrLangParser.PrintableSubstitutionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableSubstitution}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableSubstitution(StrLangParser.PrintableSubstitutionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableVariable}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableVariable(StrLangParser.PrintableVariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableVariable}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableVariable(StrLangParser.PrintableVariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableTrim}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableTrim(StrLangParser.PrintableTrimContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableTrim}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableTrim(StrLangParser.PrintableTrimContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableParenthesis}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableParenthesis(StrLangParser.PrintableParenthesisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableParenthesis}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableParenthesis(StrLangParser.PrintableParenthesisContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableRemove}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableRemove(StrLangParser.PrintableRemoveContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableRemove}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableRemove(StrLangParser.PrintableRemoveContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableInput}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableInput(StrLangParser.PrintableInputContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableInput}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableInput(StrLangParser.PrintableInputContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printableConcat}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void enterPrintableConcat(StrLangParser.PrintableConcatContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printableConcat}
	 * labeled alternative in {@link StrLangParser#printable}.
	 * @param ctx the parse tree
	 */
	void exitPrintableConcat(StrLangParser.PrintableConcatContext ctx);
}