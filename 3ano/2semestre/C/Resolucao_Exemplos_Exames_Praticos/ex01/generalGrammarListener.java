// Generated from generalGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link generalGrammarParser}.
 */
public interface generalGrammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link generalGrammarParser#main}.
	 * @param ctx the parse tree
	 */
	void enterMain(generalGrammarParser.MainContext ctx);
	/**
	 * Exit a parse tree produced by {@link generalGrammarParser#main}.
	 * @param ctx the parse tree
	 */
	void exitMain(generalGrammarParser.MainContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatPrint}
	 * labeled alternative in {@link generalGrammarParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatPrint(generalGrammarParser.StatPrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatPrint}
	 * labeled alternative in {@link generalGrammarParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatPrint(generalGrammarParser.StatPrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StatAssigment}
	 * labeled alternative in {@link generalGrammarParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStatAssigment(generalGrammarParser.StatAssigmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StatAssigment}
	 * labeled alternative in {@link generalGrammarParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStatAssigment(generalGrammarParser.StatAssigmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link generalGrammarParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(generalGrammarParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link generalGrammarParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(generalGrammarParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link generalGrammarParser#assigment}.
	 * @param ctx the parse tree
	 */
	void enterAssigment(generalGrammarParser.AssigmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link generalGrammarParser#assigment}.
	 * @param ctx the parse tree
	 */
	void exitAssigment(generalGrammarParser.AssigmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link generalGrammarParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(generalGrammarParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link generalGrammarParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(generalGrammarParser.StringContext ctx);
}