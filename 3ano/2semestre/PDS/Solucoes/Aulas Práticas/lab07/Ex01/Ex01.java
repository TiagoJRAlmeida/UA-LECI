package lab07.Ex01;

import java.util.Date;

public class Ex01 {
    public static void main(String[] args) {
        // Create employee
        EmployeeInterface employee1 = new Employee("André Oliveira");
        EmployeeInterface employee2 = new Employee("Duarte Cruz");

        // Employee start
        employee1.start(new Date());
        employee2.start(new Date());

        // Employee work
        employee1.work();
        employee2.work();

        // Employee terminate
        employee1.terminate(new Date());
        employee2.terminate(new Date());

        System.out.println();
        // TeamMember class
        EmployeeInterface employee3 = new Employee("Quim Barreiros");
        TeamMember teamMember = new TeamMember(employee3);
        teamMember.start(new Date());
        teamMember.work();
        teamMember.colaborate();
        teamMember.terminate(new Date());

        System.out.println();
        // TeamLeader class
        EmployeeInterface employee4 = new Employee("Rosinha");
        TeamLeader teamLeader = new TeamLeader(employee4);
        teamLeader.start(new Date());
        teamLeader.work();
        teamLeader.plan();
        teamLeader.terminate(new Date());

        System.out.println();
        // Manager class
        EmployeeInterface employee5 = new Employee("Rosinha");
        Manager manager = new Manager(employee5);
        manager.start(new Date());
        manager.work();
        manager.manage();
        manager.terminate(new Date());

        System.out.println();
        // Test all
        EmployeeInterface employee6 = new Employee("Toy");
        Manager managerTest = new Manager(new TeamLeader(new TeamMember(employee6)));
        managerTest.start(new Date());
        managerTest.work();
        managerTest.manage();
        managerTest.terminate(new Date());
    }
}
