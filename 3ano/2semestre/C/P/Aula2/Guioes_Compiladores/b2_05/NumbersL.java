import java.util.HashMap;
import java.util.Map;

import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ErrorNode;
import org.antlr.v4.runtime.tree.TerminalNode;
@SuppressWarnings("CheckReturnValue")

public class NumbersL extends NumbersBaseListener {

   @Override public void enterFile(NumbersParser.FileContext ctx) {
   }

   @Override public void exitFile(NumbersParser.FileContext ctx) {
   }

   @Override public void enterLine(NumbersParser.LineContext ctx) {
   }

   @Override public void exitLine(NumbersParser.LineContext ctx) {
      Integer number = Integer.parseInt(ctx.NUM.getText());
      String name = ctx.NAME.getText();

      if(exists(name)){
         System.out.println("Name already introduced");
         System.exit(1);
      }

      mapa.put(name, number);
   }

   @Override public void enterEveryRule(ParserRuleContext ctx) {
   }

   @Override public void exitEveryRule(ParserRuleContext ctx) {
   }

   @Override public void visitTerminal(TerminalNode node) {
   }

   @Override public void visitErrorNode(ErrorNode node) {
   }

   public boolean exists(String name){
      if(name == null){
         System.out.println("Name is null");
         return false;
      }
      return mapa.containsKey(name);
   }

   public Integer getValue(String name){
      if(!exists(name)){
         System.out.println("Name is not in map");
         return null;
      }
      return mapa.get(name);
   }

   Map<String,Integer> mapa = new HashMap<>();
}
