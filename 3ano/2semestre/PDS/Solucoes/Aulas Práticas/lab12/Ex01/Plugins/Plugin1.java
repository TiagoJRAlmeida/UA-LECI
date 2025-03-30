package lab12.Ex01.Plugins;

import lab12.Ex01.IPlugin;

public class Plugin1 implements IPlugin {

    @Override
    public void fazQualQuerCoisa() {
        System.out.println("Faço alguma coisa random (Plugin1)");
    }

}
