from pympler import muppy
if __name__ == '__main__':
    all_objects = muppy.get_objects()
    len(all_objects)
    28667
    from pympler import summary

    suml = summary.summarize(all_objects)
    summary.print_(suml)