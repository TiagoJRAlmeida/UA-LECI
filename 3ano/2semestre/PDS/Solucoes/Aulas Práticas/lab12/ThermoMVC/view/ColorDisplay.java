package lab12.ThermoMVC.view;

import java.awt.Color;

import javax.swing.JPanel;

import lab12.ThermoMVC.model.Thermometer;
import lab12.ThermoMVC.model.ThermometerListener;

public class ColorDisplay extends JPanel implements ThermometerListener {
    // The label displaying the color
    private JPanel tempPanel;

    /** The thermometer whose temperature is being displayed */
    protected Thermometer thermometer;

    /**
     * Creates a color thermometer
     * 
     * @param t the thermometer whose temperature is displayed
     */
    public ColorDisplay(Thermometer t) {
        thermometer = t;
        tempPanel = new JPanel();
        tempPanel.setOpaque(true);
        tempPanel.setBackground(getDisplayColor());
        add(tempPanel);
    }

    @Override
    public void temperatureChanged() {
        tempPanel.setBackground(getDisplayColor());
        repaint();
    }

    private Color getDisplayColor() {
        int temp = thermometer.getTemperature();
        if (temp <= 32)
            return new Color(0, 0, 255);
        else if (temp <= 39)
            return new Color(0, 50, 255);
        else if (temp <= 46)
            return new Color(0, 100, 255);
        else if (temp <= 54)
            return new Color(0, 150, 255);
        else if (temp <= 61)
            return new Color(0, 200, 255);
        else if (temp <= 68)
            return new Color(0, 255, 255);
        else if (temp <= 72)
            return new Color(50, 255, 0);
        else if (temp <= 75)
            return new Color(100, 255, 0);
        else if (temp <= 79)
            return new Color(150, 255, 0);
        else if (temp <= 82)
            return new Color(200, 255, 0);
        else if (temp <= 86)
            return new Color(255, 255, 0);
        else if (temp <= 91)
            return new Color(255, 200, 0);
        else if (temp <= 97)
            return new Color(255, 150, 0);
        else if (temp <= 102)
            return new Color(255, 100, 00);
        else if (temp <= 108)
            return new Color(255, 50, 0);
        return new Color(255, 0, 0);
    }
}
