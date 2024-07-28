package Study_codes.Java;
import javax.swing.*;

public class SimpleForm {
    public static void main(String[] args) {
        // Cria um novo frame
        JFrame frame = new JFrame("Formulário Simples");

        // Configura o tamanho do frame
        frame.setSize(300, 200);

        // Define o comportamento de fechar o frame
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Cria um painel para organizar os componentes
        JPanel panel = new JPanel();

        // Adiciona o painel ao frame
        frame.add(panel);

        // Chama um método para adicionar os componentes ao painel
        placeComponents(panel);

        // Torna o frame visível
        frame.setVisible(true);
    }

    private static void placeComponents(JPanel panel) {
        // Define o layout como null para posicionamento manual
        panel.setLayout(null);

        // Cria uma etiqueta para o nome
        JLabel userLabel = new JLabel("Nome:");
        userLabel.setBounds(10, 20, 80, 25);
        panel.add(userLabel);

        // Cria um campo de texto para o nome
        JTextField userText = new JTextField(20);
        userText.setBounds(100, 20, 165, 25);
        panel.add(userText);

        // Cria uma etiqueta para a senha
        JLabel passwordLabel = new JLabel("Senha:");
        passwordLabel.setBounds(10, 50, 80, 25);
        panel.add(passwordLabel);

        // Cria um campo de texto para a senha
        JPasswordField passwordText = new JPasswordField(20);
        passwordText.setBounds(100, 50, 165, 25);
        panel.add(passwordText);

        // Cria um botão de login
        JButton loginButton = new JButton("Login");
        loginButton.setBounds(10, 80, 80, 25);
        panel.add(loginButton);
    }
}
