// Generated from /home/tiago/github/UA-LECI/3ano/2semestre/C/Exemplos_Exames_Praticos/ex1/StrLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class StrLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		QUOTED_STR=10, VARIABLE=11, WS=12, LINE_COMMENT=13;
	public static final int
		RULE_program = 0, RULE_stat = 1, RULE_printable = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stat", "printable"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'print'", "':'", "'+'", "'-'", "'trim'", "'('", "')'", "'/'", 
			"'input'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "QUOTED_STR", 
			"VARIABLE", "WS", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "StrLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public StrLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(StrLangParser.EOF, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==VARIABLE) {
				{
				{
				setState(6);
				stat();
				}
				}
				setState(11);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(12);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatPrintContext extends StatContext {
		public PrintableContext printable() {
			return getRuleContext(PrintableContext.class,0);
		}
		public StatPrintContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterStatPrint(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitStatPrint(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class StatAssignContext extends StatContext {
		public TerminalNode VARIABLE() { return getToken(StrLangParser.VARIABLE, 0); }
		public PrintableContext printable() {
			return getRuleContext(PrintableContext.class,0);
		}
		public StatAssignContext(StatContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterStatAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitStatAssign(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			setState(19);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new StatPrintContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(14);
				match(T__0);
				setState(15);
				printable(0);
				}
				break;
			case VARIABLE:
				_localctx = new StatAssignContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(16);
				match(VARIABLE);
				setState(17);
				match(T__1);
				setState(18);
				printable(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintableContext extends ParserRuleContext {
		public PrintableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printable; }
	 
		public PrintableContext() { }
		public void copyFrom(PrintableContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableStringContext extends PrintableContext {
		public TerminalNode QUOTED_STR() { return getToken(StrLangParser.QUOTED_STR, 0); }
		public PrintableStringContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableString(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableSubstitutionContext extends PrintableContext {
		public PrintableContext p1;
		public PrintableContext p2;
		public PrintableContext p3;
		public List<PrintableContext> printable() {
			return getRuleContexts(PrintableContext.class);
		}
		public PrintableContext printable(int i) {
			return getRuleContext(PrintableContext.class,i);
		}
		public PrintableSubstitutionContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableSubstitution(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableSubstitution(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableVariableContext extends PrintableContext {
		public TerminalNode VARIABLE() { return getToken(StrLangParser.VARIABLE, 0); }
		public PrintableVariableContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableVariable(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableTrimContext extends PrintableContext {
		public PrintableContext printable() {
			return getRuleContext(PrintableContext.class,0);
		}
		public PrintableTrimContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableTrim(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableTrim(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableParenthesisContext extends PrintableContext {
		public PrintableContext printable() {
			return getRuleContext(PrintableContext.class,0);
		}
		public PrintableParenthesisContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableParenthesis(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableParenthesis(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableRemoveContext extends PrintableContext {
		public List<PrintableContext> printable() {
			return getRuleContexts(PrintableContext.class);
		}
		public PrintableContext printable(int i) {
			return getRuleContext(PrintableContext.class,i);
		}
		public PrintableRemoveContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableRemove(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableRemove(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableInputContext extends PrintableContext {
		public PrintableContext printable() {
			return getRuleContext(PrintableContext.class,0);
		}
		public PrintableInputContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableInput(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableInput(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintableConcatContext extends PrintableContext {
		public List<PrintableContext> printable() {
			return getRuleContexts(PrintableContext.class);
		}
		public PrintableContext printable(int i) {
			return getRuleContext(PrintableContext.class,i);
		}
		public PrintableConcatContext(PrintableContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).enterPrintableConcat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof StrLangListener ) ((StrLangListener)listener).exitPrintableConcat(this);
		}
	}

	public final PrintableContext printable() throws RecognitionException {
		return printable(0);
	}

	private PrintableContext printable(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		PrintableContext _localctx = new PrintableContext(_ctx, _parentState);
		PrintableContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_printable, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__4:
				{
				_localctx = new PrintableTrimContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(22);
				match(T__4);
				setState(23);
				printable(6);
				}
				break;
			case T__5:
				{
				_localctx = new PrintableParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(24);
				match(T__5);
				setState(25);
				printable(0);
				setState(26);
				match(T__6);
				}
				break;
			case T__8:
				{
				_localctx = new PrintableInputContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(28);
				match(T__8);
				setState(29);
				match(T__5);
				setState(30);
				printable(0);
				setState(31);
				match(T__6);
				}
				break;
			case VARIABLE:
				{
				_localctx = new PrintableVariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(33);
				match(VARIABLE);
				}
				break;
			case QUOTED_STR:
				{
				_localctx = new PrintableStringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(34);
				match(QUOTED_STR);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(51);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(49);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new PrintableConcatContext(new PrintableContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_printable);
						setState(37);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(38);
						match(T__2);
						setState(39);
						printable(9);
						}
						break;
					case 2:
						{
						_localctx = new PrintableRemoveContext(new PrintableContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_printable);
						setState(40);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(41);
						match(T__3);
						setState(42);
						printable(8);
						}
						break;
					case 3:
						{
						_localctx = new PrintableSubstitutionContext(new PrintableContext(_parentctx, _parentState));
						((PrintableSubstitutionContext)_localctx).p1 = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_printable);
						setState(43);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(44);
						match(T__7);
						setState(45);
						((PrintableSubstitutionContext)_localctx).p2 = printable(0);
						setState(46);
						match(T__7);
						setState(47);
						((PrintableSubstitutionContext)_localctx).p3 = printable(5);
						}
						break;
					}
					} 
				}
				setState(53);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return printable_sempred((PrintableContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean printable_sempred(PrintableContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 8);
		case 1:
			return precpred(_ctx, 7);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\r7\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0005\u0000\b\b\u0000\n\u0000\f\u0000\u000b"+
		"\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0003\u0001\u0014\b\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002$\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0005\u00022\b\u0002\n\u0002\f\u00025\t\u0002\u0001"+
		"\u0002\u0000\u0001\u0004\u0003\u0000\u0002\u0004\u0000\u0000<\u0000\t"+
		"\u0001\u0000\u0000\u0000\u0002\u0013\u0001\u0000\u0000\u0000\u0004#\u0001"+
		"\u0000\u0000\u0000\u0006\b\u0003\u0002\u0001\u0000\u0007\u0006\u0001\u0000"+
		"\u0000\u0000\b\u000b\u0001\u0000\u0000\u0000\t\u0007\u0001\u0000\u0000"+
		"\u0000\t\n\u0001\u0000\u0000\u0000\n\f\u0001\u0000\u0000\u0000\u000b\t"+
		"\u0001\u0000\u0000\u0000\f\r\u0005\u0000\u0000\u0001\r\u0001\u0001\u0000"+
		"\u0000\u0000\u000e\u000f\u0005\u0001\u0000\u0000\u000f\u0014\u0003\u0004"+
		"\u0002\u0000\u0010\u0011\u0005\u000b\u0000\u0000\u0011\u0012\u0005\u0002"+
		"\u0000\u0000\u0012\u0014\u0003\u0004\u0002\u0000\u0013\u000e\u0001\u0000"+
		"\u0000\u0000\u0013\u0010\u0001\u0000\u0000\u0000\u0014\u0003\u0001\u0000"+
		"\u0000\u0000\u0015\u0016\u0006\u0002\uffff\uffff\u0000\u0016\u0017\u0005"+
		"\u0005\u0000\u0000\u0017$\u0003\u0004\u0002\u0006\u0018\u0019\u0005\u0006"+
		"\u0000\u0000\u0019\u001a\u0003\u0004\u0002\u0000\u001a\u001b\u0005\u0007"+
		"\u0000\u0000\u001b$\u0001\u0000\u0000\u0000\u001c\u001d\u0005\t\u0000"+
		"\u0000\u001d\u001e\u0005\u0006\u0000\u0000\u001e\u001f\u0003\u0004\u0002"+
		"\u0000\u001f \u0005\u0007\u0000\u0000 $\u0001\u0000\u0000\u0000!$\u0005"+
		"\u000b\u0000\u0000\"$\u0005\n\u0000\u0000#\u0015\u0001\u0000\u0000\u0000"+
		"#\u0018\u0001\u0000\u0000\u0000#\u001c\u0001\u0000\u0000\u0000#!\u0001"+
		"\u0000\u0000\u0000#\"\u0001\u0000\u0000\u0000$3\u0001\u0000\u0000\u0000"+
		"%&\n\b\u0000\u0000&\'\u0005\u0003\u0000\u0000\'2\u0003\u0004\u0002\t("+
		")\n\u0007\u0000\u0000)*\u0005\u0004\u0000\u0000*2\u0003\u0004\u0002\b"+
		"+,\n\u0004\u0000\u0000,-\u0005\b\u0000\u0000-.\u0003\u0004\u0002\u0000"+
		"./\u0005\b\u0000\u0000/0\u0003\u0004\u0002\u000502\u0001\u0000\u0000\u0000"+
		"1%\u0001\u0000\u0000\u00001(\u0001\u0000\u0000\u00001+\u0001\u0000\u0000"+
		"\u000025\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000034\u0001\u0000"+
		"\u0000\u00004\u0005\u0001\u0000\u0000\u000053\u0001\u0000\u0000\u0000"+
		"\u0005\t\u0013#13";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}