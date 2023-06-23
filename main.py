def main():
    num_males = int((input('Number of males?: ')))
    num_females = int((input('Number of females?: ')))
    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    total = int(num_males + num_females)
    m_perc = float(num_males / total) * 100
    f_perc = float(num_females / total) * 100
    print(f'Tne total number of students:', total)
    print(f'The total number of males and females: ', num_males, num_females)
    print(f'The percentage of males and females:', (format(num_males, ".2f")) + "%", (format(num_females, ".2f")) + "%")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
