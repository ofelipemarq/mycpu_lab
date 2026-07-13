from cpu import CPU


def main():
    cpu = CPU()

    program = [
        ("LOAD", "R1", 10),
        ("LOAD", "R2", 20),
        ("ADD", "R1", "R2"),
        ("HALT",),
    ]

    cpu.load_program(program)

    cpu.dump_program()
    cpu.dump_state()


if __name__ == "__main__":
    main()