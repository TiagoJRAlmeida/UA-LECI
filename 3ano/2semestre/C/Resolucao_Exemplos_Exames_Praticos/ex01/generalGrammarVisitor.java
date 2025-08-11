// Generated from generalGrammar.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link generalGrammarParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface generalGrammarVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link generalGrammarParser#main}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMain(generalGrammarParser.MainContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatPrint}
	 * labeled alternative in {@link generalGrammarParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatPrint(generalGrammarParser.StatPrintContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StatAssigment}
	 * labeled alternative in {@link generalGrammarParser#stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatAssigment(generalGrammarParser.StatAssigmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link generalGrammarParser#print}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrint(generalGrammarParser.PrintContext ctx);
	/**
	 * Visit a parse tree produced by {@link generalGrammarParser#assigment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssigment(generalGrammarParser.AssigmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link generalGrammarParser#string}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitString(generalGrammarParser.StringContext ctx);
}